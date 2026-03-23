#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anima AIOS v6.0 - Distill Engine

L2→L3 提炼引擎：从情景记忆中提取语义知识。
引入 LLM 进行质量评估、去重分析和知识提炼。

Author: 清禾
Date: 2026-03-23
Version: 6.0.0
"""

import os
import json
import logging
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from fact_store import FactStore, Fact, QualityGrade

logger = logging.getLogger(__name__)


class LLMClient:
    """
    LLM 调用客户端
    
    默认使用当前 Agent 的模型（通过 OpenClaw 的 sessions_spawn 或直接调用）。
    支持多模型配置，可按任务指定不同模型。
    """
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.provider = self.config.get("provider", "current_agent")
        self.models = self.config.get("models", {})
    
    def call(self, prompt: str, task: str = "default", max_tokens: int = 500) -> str:
        """
        调用 LLM
        
        Args:
            prompt: 提示词
            task: 任务类型（quality_assess / dedup_analyze / palace_classify / distill）
            max_tokens: 最大输出 token 数
        
        Returns:
            LLM 响应文本
        """
        model = self.models.get(task, self.provider)
        
        # 方案1：通过 OpenClaw 的命令行工具调用（最通用）
        try:
            result = subprocess.run(
                ["openclaw", "ask", "--raw", prompt],
                capture_output=True, text=True, timeout=30,
                env={**os.environ, "OPENCLAW_MAX_TOKENS": str(max_tokens)}
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        
        # 方案2：降级为规则匹配
        logger.warning(f"LLM 调用失败，降级为规则模式 (task={task})")
        return ""


class DistillEngine:
    """
    L2→L3 提炼引擎
    
    工作流程：
    1. 扫描 L2 中 quality=pending 的 facts
    2. LLM 质量评估（S/A/B/C）
    3. B 级及以上的 facts 进入提炼候选
    4. LLM 去重检查（与已有 L3 对比）
    5. LLM 知识提炼（提取核心知识）
    6. 写入 L3 语义记忆
    """
    
    def __init__(self, agent_name: str, facts_base: str = "/home/画像",
                 llm_config: Dict = None):
        self.agent_name = agent_name
        self.facts_base = facts_base
        self.store = FactStore(agent_name, facts_base)
        self.llm = LLMClient(llm_config)
        
        # 提炼配置
        self.min_quality = "B"  # 最低提炼质量
        self.quality_order = {"S": 4, "A": 3, "B": 2, "C": 1, "pending": 0}
    
    def assess_quality(self, fact: Fact) -> QualityGrade:
        """
        LLM 质量评估
        
        Args:
            fact: 待评估的 L2 fact
        
        Returns:
            质量等级 S/A/B/C
        """
        prompt = f"""请评估以下 AI Agent 记忆片段的质量，从 S/A/B/C 四个等级中选择一个。

评估标准：
- S（极高）：包含重要决策、架构设计、关键教训，对长期成长有重大价值
- A（高）：包含有价值的技术知识、项目经验、问题解决方案
- B（中）：包含有用的日常记录、工作进展、学习笔记
- C（低）：琐碎信息、重复内容、临时备忘

记忆内容：
{fact.content[:500]}

请只回复一个字母（S/A/B/C），不要其他内容。"""
        
        response = self.llm.call(prompt, task="quality_assess", max_tokens=5)
        
        grade = response.strip().upper()
        if grade in ("S", "A", "B", "C"):
            return grade
        
        # LLM 降级：规则评估
        return self._rule_based_quality(fact)
    
    def _rule_based_quality(self, fact: Fact) -> QualityGrade:
        """规则降级：基于内容长度和关键词评估质量"""
        content = fact.content
        length = len(content)
        
        # 关键词权重
        high_value_keywords = ["决策", "架构", "设计", "教训", "方案", "原则", "铁律",
                               "decision", "architecture", "design", "lesson", "principle"]
        mid_value_keywords = ["解决", "修复", "实现", "学到", "发现", "优化",
                              "fix", "implement", "learn", "optimize"]
        
        score = 0
        for kw in high_value_keywords:
            if kw in content:
                score += 3
        for kw in mid_value_keywords:
            if kw in content:
                score += 1
        
        if length > 200:
            score += 2
        elif length > 100:
            score += 1
        
        if score >= 6:
            return "S"
        elif score >= 4:
            return "A"
        elif score >= 2:
            return "B"
        else:
            return "C"
    
    def check_duplicate(self, content: str, existing_semantics: List[Fact]) -> Tuple[bool, Optional[str]]:
        """
        LLM 去重检查
        
        Args:
            content: 待检查的内容
            existing_semantics: 已有的 L3 语义记忆列表
        
        Returns:
            (是否重复, 重复的 fact_id)
        """
        if not existing_semantics:
            return False, None
        
        # 取最近的 20 条 L3 做对比
        recent = existing_semantics[:20]
        existing_summaries = "\n".join([
            f"[{f.fact_id}] {f.content[:100]}" for f in recent
        ])
        
        prompt = f"""请判断以下新内容是否与已有知识重复或高度相似。

新内容：
{content[:300]}

已有知识：
{existing_summaries}

如果重复或高度相似，回复 "DUPLICATE: <fact_id>"。
如果不重复，回复 "UNIQUE"。
只回复上述格式，不要其他内容。"""
        
        response = self.llm.call(prompt, task="dedup_analyze", max_tokens=50)
        
        if response.startswith("DUPLICATE:"):
            dup_id = response.replace("DUPLICATE:", "").strip()
            return True, dup_id
        
        # LLM 降级：简单字符串匹配
        if not response:
            return self._rule_based_dedup(content, existing_semantics)
        
        return False, None
    
    def _rule_based_dedup(self, content: str, existing: List[Fact]) -> Tuple[bool, Optional[str]]:
        """规则降级：基于关键词重叠率去重"""
        content_words = set(content.lower().split())
        
        for fact in existing[:20]:
            fact_words = set(fact.content.lower().split())
            if not fact_words:
                continue
            overlap = len(content_words & fact_words) / max(len(content_words), 1)
            if overlap > 0.7:
                return True, fact.fact_id
        
        return False, None
    
    def distill(self, facts: List[Fact]) -> Optional[str]:
        """
        LLM 知识提炼：从多条 L2 情景记忆中提取核心知识
        
        Args:
            facts: L2 情景记忆列表
        
        Returns:
            提炼后的知识内容，如果无法提炼则返回 None
        """
        if not facts:
            return None
        
        # 单条直接提取
        if len(facts) == 1:
            content = facts[0].content
            prompt = f"""请从以下 AI Agent 的工作记录中提取核心知识点。
去掉时间、人物等细节，保留可复用的知识、经验、教训或决策。
用简洁的语言总结，不超过 200 字。

原始记录：
{content[:500]}

请直接输出提炼后的知识，不要加前缀。"""
        else:
            combined = "\n---\n".join([f.content[:300] for f in facts[:5]])
            prompt = f"""请从以下多条 AI Agent 工作记录中提炼核心知识。
找出共同主题、规律或教训，用简洁的语言总结。不超过 300 字。

记录：
{combined}

请直接输出提炼后的知识，不要加前缀。"""
        
        response = self.llm.call(prompt, task="distill", max_tokens=400)
        
        if response and len(response) > 10:
            return response
        
        # LLM 降级：取最长的一条作为知识
        if facts:
            longest = max(facts, key=lambda f: len(f.content))
            return longest.content[:300]
        
        return None
    
    def run(self, batch_size: int = 20, dry_run: bool = False) -> Dict:
        """
        执行一轮提炼
        
        Args:
            batch_size: 每轮处理的最大 fact 数
            dry_run: 仅评估不写入
        
        Returns:
            提炼统计
        """
        stats = {
            "scanned": 0,
            "assessed": 0,
            "quality_distribution": {"S": 0, "A": 0, "B": 0, "C": 0},
            "distilled": 0,
            "duplicates_skipped": 0,
            "errors": 0
        }
        
        # 1. 扫描 pending 的 L2 facts
        pending_facts = self.store.list_facts("episodic", quality="pending", limit=batch_size)
        stats["scanned"] = len(pending_facts)
        
        if not pending_facts:
            logger.info("没有待处理的 L2 facts")
            return stats
        
        logger.info(f"扫描到 {len(pending_facts)} 条待评估的 L2 facts")
        
        # 2. 获取已有 L3 用于去重
        existing_semantics = self.store.list_facts("semantic", limit=50)
        
        # 3. 逐条处理
        candidates = []
        
        for fact in pending_facts:
            try:
                # 质量评估
                quality = self.assess_quality(fact)
                stats["assessed"] += 1
                stats["quality_distribution"][quality] += 1
                
                # 更新质量
                if not dry_run:
                    self.store.update_quality(fact.fact_id, "episodic", quality)
                
                logger.debug(f"质量评估: {fact.fact_id} → {quality}")
                
                # B 级及以上进入候选
                if self.quality_order.get(quality, 0) >= self.quality_order[self.min_quality]:
                    candidates.append(fact)
                    
            except Exception as e:
                logger.warning(f"处理 fact 失败 {fact.fact_id}: {e}")
                stats["errors"] += 1
        
        logger.info(f"质量评估完成: {stats['quality_distribution']}，{len(candidates)} 条进入提炼候选")
        
        # 4. 对候选逐条提炼
        for fact in candidates:
            try:
                # 提炼知识
                knowledge = self.distill([fact])
                if not knowledge:
                    continue
                
                # 去重检查
                is_dup, dup_id = self.check_duplicate(knowledge, existing_semantics)
                if is_dup:
                    logger.debug(f"跳过重复: {fact.fact_id} ≈ {dup_id}")
                    stats["duplicates_skipped"] += 1
                    continue
                
                # 写入 L3
                if not dry_run:
                    new_fact = self.store.create_semantic(
                        content=knowledge,
                        source_facts=[fact.fact_id],
                        tags=fact.tags + ["distilled"],
                        quality=fact.quality
                    )
                    # 加入已有列表（后续去重用）
                    existing_semantics.insert(0, new_fact)
                    logger.info(f"提炼完成: {fact.fact_id} → {new_fact.fact_id}")
                
                stats["distilled"] += 1
                
            except Exception as e:
                logger.warning(f"提炼失败 {fact.fact_id}: {e}")
                stats["errors"] += 1
        
        logger.info(f"提炼完成: 扫描 {stats['scanned']}，评估 {stats['assessed']}，"
                     f"提炼 {stats['distilled']}，跳过重复 {stats['duplicates_skipped']}")
        
        return stats


def main():
    """命令行入口"""
    import argparse
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [DistillEngine] %(levelname)s: %(message)s'
    )
    
    parser = argparse.ArgumentParser(description='Anima Distill Engine - L2→L3 知识提炼')
    parser.add_argument('--agent', type=str, default='', help='Agent 名称')
    parser.add_argument('--facts-base', type=str, default='/home/画像', help='Facts 基础路径')
    parser.add_argument('--batch-size', type=int, default=20, help='每轮处理数量')
    parser.add_argument('--dry-run', action='store_true', help='仅评估不写入')
    parser.add_argument('--stats', action='store_true', help='显示统计信息')
    args = parser.parse_args()
    
    agent_name = args.agent or os.getenv("ANIMA_AGENT_NAME", "unknown")
    facts_base = os.getenv("ANIMA_FACTS_BASE", args.facts_base)
    
    engine = DistillEngine(agent_name, facts_base)
    
    if args.stats:
        episodic_count = engine.store.count("episodic")
        semantic_count = engine.store.count("semantic")
        pending = engine.store.list_facts("episodic", quality="pending")
        print(f"Agent: {agent_name}")
        print(f"L2 情景记忆: {episodic_count}")
        print(f"L3 语义记忆: {semantic_count}")
        print(f"待评估: {len(pending)}")
        return
    
    stats = engine.run(batch_size=args.batch_size, dry_run=args.dry_run)
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
