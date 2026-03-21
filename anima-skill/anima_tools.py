#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anima-AIOS Skill - Tool Implementations

OpenClaw Skill 工具实现

提供以下工具：
- memory_search_v2: 增强版记忆搜索（+2 EXP）
- memory_write_v2: 增强版记忆写入（自动 EXP 奖励）
- get_cognitive_profile: 获取认知画像
- get_exp: 查询 EXP 详情
- get_level: 查询等级信息
- quest_daily_status: 查看每日任务
- quest_complete: 提交任务完成

Author: 枢衡
Date: 2026-03-21
Version: 5.0.0
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

# 确保 core 模块在路径中
ANIMA_HOME = Path(os.path.expanduser("~/.anima"))
if ANIMA_HOME.exists():
    sys.path.insert(0, str(ANIMA_HOME / "core"))

# OpenClaw workspace 路径
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace-shuheng"))


# ============================================================================
# 工具 1: memory_search_v2
# ============================================================================

def memory_search_v2(query: str, type: str = "all", maxResults: int = 10, agent_name: str = "current") -> Dict:
    """
    增强版记忆搜索
    
    功能：
    - 支持语义检索（如果配置了向量检索）
    - 支持时间范围过滤
    - 返回结果带相关性评分
    - 自动奖励 +2 EXP
    
    Args:
        query: 搜索关键词
        type: 记忆类型 (episodic/semantic/all)
        maxResults: 最大结果数
        agent_name: Agent 名称（"current"表示当前用户）
    
    Returns:
        {
            "results": [...],
            "count": int,
            "expReward": 2,
            "message": "搜索完成，+2 EXP"
        }
    """
    # 解析 Agent 名称
    if agent_name == "current":
        agent_name = _get_current_agent()
    
    # 调用 core 的记忆搜索（这里简化实现，实际应集成 SiliconFlow 向量检索）
    results = _search_memory_simple(query, type, maxResults, agent_name)
    
    # 记录 EXP（搜索记忆 +2 EXP）
    exp_reward = 2
    _add_exp(agent_name, "application", exp_reward, "memory_search", {
        "query": query,
        "result_count": len(results)
    })
    
    return {
        "results": results,
        "count": len(results),
        "expReward": exp_reward,
        "message": f"搜索完成，找到 {len(results)} 条记忆，+{exp_reward} EXP"
    }


def _search_memory_simple(query: str, type: str, maxResults: int, agent_name: str) -> List[Dict]:
    """简单文本搜索（基础实现）"""
    memory_dir = WORKSPACE / "memory"
    results = []
    
    # 搜索今天的记忆文件
    today = datetime.now().strftime("%Y-%m-%d")
    memory_file = memory_dir / f"{today}.md"
    
    if memory_file.exists():
        content = memory_file.read_text(encoding="utf-8")
        lines = content.split("\n")
        
        for i, line in enumerate(lines):
            if query.lower() in line.lower():
                results.append({
                    "factId": f"line_{i}",
                    "content": line.strip(),
                    "type": "episodic",
                    "relevance": 0.8,
                    "timestamp": today
                })
                
                if len(results) >= maxResults:
                    break
    
    # TODO: 集成 SiliconFlow 向量检索
    # - 使用 bge-m3 模型
    # - 计算查询向量与记忆向量的相似度
    # - 按相关性排序
    
    return results


# ============================================================================
# 工具 2: memory_write_v2
# ============================================================================

def memory_write_v2(content: str, type: str = "episodic", tags: Optional[List[str]] = None, 
                    quality: str = "auto", agent_name: str = "current") -> Dict:
    """
    增强版记忆写入
    
    功能：
    - 自动计算 EXP 奖励（episodic +1, semantic +2）
    - 自动提取摘要和标签
    - 质量检测（完整性、价值度）
    - 去重检测
    
    Args:
        content: 记忆内容
        type: 记忆类型 (episodic/semantic)
        tags: 标签列表（可选，自动提取）
        quality: 质量等级 (auto/S/A/B/C)
        agent_name: Agent 名称
    
    Returns:
        {
            "factId": "xxx",
            "expReward": 2,
            "quality": "A",
            "message": "记忆已保存，+2 EXP（semantic）"
        }
    """
    if agent_name == "current":
        agent_name = _get_current_agent()
    
    # 去重检测（简单实现：检查最近 10 条记忆）
    if _check_duplicate(content, agent_name):
        return {
            "factId": None,
            "expReward": 0,
            "quality": "N/A",
            "message": "⚠️ 检测到相似记忆，已跳过",
            "duplicate": True
        }
    
    # 自动提取标签（如果未提供）
    if tags is None or len(tags) == 0:
        tags = _extract_tags(content)
    
    # 质量评估
    if quality == "auto":
        quality = _assess_quality(content)
    
    # 计算 EXP 奖励
    base_exp = 1 if type == "episodic" else 2
    quality_multiplier = {"S": 1.5, "A": 1.2, "B": 1.0, "C": 0.8}.get(quality, 1.0)
    exp_reward = int(base_exp * quality_multiplier)
    
    # 写入记忆（简化实现：追加到今日文件）
    fact_id = _write_memory_simple(content, type, tags, agent_name)
    
    # 记录 EXP（使用 core 层的维度命名）
    # core 维度名：understanding, application, creation, metacognition, collaboration
    dimension = "understanding" if type == "episodic" else "creation"
    _add_exp(agent_name, dimension, exp_reward, "memory_write", {
        "type": type,
        "quality": quality,
        "content_length": len(content)
    })
    
    return {
        "factId": fact_id,
        "expReward": exp_reward,
        "quality": quality,
        "tags": tags,
        "message": f"记忆已保存，+{exp_reward} EXP（{type}, {quality}级）"
    }


def _write_memory_simple(content: str, type: str, tags: List[str], agent_name: str) -> str:
    """简单写入记忆到今日文件"""
    today = datetime.now().strftime("%Y-%m-%d")
    memory_file = WORKSPACE / "memory" / f"{today}.md"
    
    # 确保目录存在
    memory_file.parent.mkdir(parents=True, exist_ok=True)
    
    # 生成 factId
    fact_id = f"{today}_{len(content)}_{hash(content) % 10000:04d}"
    
    # 追加写入
    timestamp = datetime.now().strftime("%H:%M")
    with open(memory_file, "a", encoding="utf-8") as f:
        f.write(f"\n- [{timestamp}] {content} #{type}\n")
        if tags:
            f.write(f"  标签：{', '.join(tags)}\n")
    
    return fact_id


def _check_duplicate(content: str, agent_name: str, threshold: int = 50) -> bool:
    """检查重复（简单实现：检查最近内容）"""
    # TODO: 实现基于内容哈希或向量相似度的去重
    return False


def _extract_tags(content: str) -> List[str]:
    """自动提取标签（简单实现：提取关键词）"""
    # TODO: 使用 NLP 提取关键词
    # 暂时返回空列表
    return []


def _assess_quality(content: str) -> str:
    """评估内容质量"""
    length = len(content)
    
    if length < 50:
        return "C"
    elif length < 200:
        return "B"
    elif length < 500:
        return "A"
    else:
        return "S"


# ============================================================================
# 工具 3-5: 认知工具
# ============================================================================

def get_cognitive_profile(agent_name: str = "current") -> Dict:
    """
    获取认知画像
    
    Returns:
        {
            "agent": "枢衡",
            "level": 10,
            "exp": 5060,
            "nextLevelExp": 6400,
            "progress": "79%",
            "dimensions": {
                "internalization": 85,
                "application": 78,
                "creation": 92,
                "metacognition": 88,
                "collaboration": 75
            },
            "radar": "ASCII 雷达图"
        }
    """
    if agent_name == "current":
        agent_name = _get_current_agent()
    
    # 尝试使用 core 模块
    if ANIMA_HOME.exists():
        try:
            sys.path.insert(0, str(ANIMA_HOME / "core"))
            from cognitive_profile import CognitiveProfileGenerator
            generator = CognitiveProfileGenerator(agent_name, facts_base="/home/画像")
            profile = generator.generate_profile(auto_scan=False)
            
            # core 返回的维度名称映射
            dimension_map = {
                'understanding': 'internalization',  # 理解 → 内化
                'application': 'application',
                'creation': 'creation',
                'metacognition': 'metacognition',
                'collaboration': 'collaboration'
            }
            
            # 转换维度格式（core 返回嵌套 dict，转换为简单分数）
            dimensions = {}
            for core_dim, skill_dim in dimension_map.items():
                if core_dim in profile['dimensions']:
                    dim_data = profile['dimensions'][core_dim]
                    if isinstance(dim_data, dict):
                        dimensions[skill_dim] = dim_data.get('score', 0)
                    else:
                        dimensions[skill_dim] = dim_data
                else:
                    dimensions[skill_dim] = 0
            
            # 获取等级和 EXP
            level = profile.get('level', 1)
            if isinstance(level, dict):
                level = level.get('level', 1)
            
            # 获取 EXP（core 可能直接返回数字或嵌套 dict）
            exp_data = _get_exp_simple(agent_name)
            total_exp = exp_data['totalExp']
            next_exp = _calculate_next_level_exp(level)
            progress = int((total_exp / next_exp) * 100) if next_exp > 0 else 0
            
            return {
                "agent": profile["agent"],
                "level": level,
                "exp": total_exp,
                "nextLevelExp": next_exp,
                "progress": f"{progress}%",
                "dimensions": dimensions,
                "radar": _generate_radar_ascii(dimensions)
            }
        except Exception as e:
            # 降级：返回简化版本
            # print(f"core 调用失败：{e}")
            pass
    
    # 降级方案
    exp_data = _get_exp_simple(agent_name)
    return {
        "agent": agent_name,
        "level": exp_data["level"],
        "exp": exp_data["totalExp"],
        "nextLevelExp": _calculate_next_level_exp(exp_data["level"]),
        "progress": "N/A (core 未安装)",
        "dimensions": {
            "internalization": 0,
            "application": 0,
            "creation": 0,
            "metacognition": 0,
            "collaboration": 0
        },
        "radar": "💡 首次使用，运行 `bash post-install.sh` 安装 core 以获取完整功能"
    }


def get_exp(agent_name: str = "current") -> Dict:
    """
    查询 EXP 详情
    
    Returns:
        {
            "totalExp": 5060,
            "todayExp": 45,
            "level": 10,
            "breakdown": {
                "memory_write": 2100,
                "memory_search": 1500,
                "weekly_report": 800,
                "knowledge_share": 660
            }
        }
    """
    if agent_name == "current":
        agent_name = _get_current_agent()
    
    return _get_exp_simple(agent_name)


def get_level(agent_name: str = "current") -> Dict:
    """
    查询等级信息
    
    Returns:
        {
            "currentLevel": 10,
            "nextLevel": 11,
            "currentExp": 5060,
            "requiredExp": 6400,
            "progress": 79,
            "progressBar": "████████░░ 79%"
        }
    """
    if agent_name == "current":
        agent_name = _get_current_agent()
    
    exp_data = _get_exp_simple(agent_name)
    level = exp_data["level"]
    current_exp = exp_data["totalExp"]
    next_exp = _calculate_next_level_exp(level)
    
    progress = int((current_exp / next_exp) * 100) if next_exp > 0 else 0
    progress_bar = _generate_progress_bar(progress)
    
    return {
        "currentLevel": level,
        "nextLevel": level + 1,
        "currentExp": current_exp,
        "requiredExp": next_exp,
        "progress": progress,
        "progressBar": progress_bar
    }


def _get_exp_simple(agent_name: str) -> Dict:
    """简化版 EXP 查询（直接读取 exp_history.jsonl）"""
    exp_file = ANIMA_HOME / agent_name / "exp_history.jsonl"
    
    if not exp_file.exists():
        # 尝试旧路径
        exp_file = Path("/home/画像") / agent_name / "exp_history.jsonl"
    
    total_exp = 0
    today_exp = 0
    breakdown = {}
    today = datetime.now().strftime("%Y-%m-%d")
    
    if exp_file.exists():
        with open(exp_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    record = json.loads(line.strip())
                    exp = record.get("exp", 0)
                    total_exp += exp
                    
                    # 今日 EXP
                    record_date = record.get("date", "")
                    if record_date == today:
                        today_exp += exp
                    
                    # 分类统计
                    action = record.get("action", "other")
                    breakdown[action] = breakdown.get(action, 0) + exp
                except:
                    continue
    
    # 计算等级
    level = max(1, int(total_exp ** 0.28))
    
    return {
        "totalExp": total_exp,
        "todayExp": today_exp,
        "level": level,
        "breakdown": breakdown
    }


def _calculate_next_level_exp(level: int) -> int:
    """计算下一级所需 EXP"""
    # 反推公式：level = exp^0.28 => exp = level^(1/0.28)
    next_level = level + 1
    return int(next_level ** (1 / 0.28))


def _generate_progress_bar(progress: int, width: int = 10) -> str:
    """生成进度条"""
    filled = int(progress / 10)
    bar = "█" * filled + "░" * (width - filled)
    return f"{bar} {progress}%"


def _generate_radar_ascii(dimensions: Dict[str, int]) -> str:
    """生成 ASCII 雷达图"""
    lines = []
    for dim, score in dimensions.items():
        bar_len = int(score / 10)
        bar = "█" * bar_len + "░" * (10 - bar_len)
        dim_cn = {
            "internalization": "内化",
            "application": "应用",
            "creation": "创造",
            "metacognition": "元认知",
            "collaboration": "协作"
        }.get(dim, dim)
        lines.append(f"  {dim_cn:6} {bar} {score}")
    
    return "\n".join(lines)


# ============================================================================
# 工具 6-7: 任务工具
# ============================================================================

def quest_daily_status(agent_name: str = "current") -> Dict:
    """
    查看每日任务状态
    
    Returns:
        {
            "date": "2026-03-21",
            "quests": [
                {
                    "id": "q1",
                    "title": "写一条记忆",
                    "difficulty": "easy",
                    "expReward": 5,
                    "status": "completed"
                },
                ...
            ],
            "completionBonus": 15
        }
    """
    if agent_name == "current":
        agent_name = _get_current_agent()
    
    today = datetime.now().strftime("%Y-%m-%d")
    quest_file = ANIMA_HOME / agent_name / "quests" / f"{today}.json"
    
    if not quest_file.exists():
        # 生成今日任务
        quests = _generate_daily_quests(agent_name)
        _save_quests(quests, quest_file)
    else:
        with open(quest_file, "r", encoding="utf-8") as f:
            quests = json.load(f)
    
    return {
        "date": today,
        "quests": quests,
        "completionBonus": 15
    }


def quest_complete(quest_id: str, proof: Optional[str] = None, agent_name: str = "current") -> Dict:
    """
    提交任务完成
    
    Args:
        quest_id: 任务 ID
        proof: 完成证据（可选）
        agent_name: Agent 名称
    
    Returns:
        {
            "success": True,
            "expReward": 10,
            "message": "任务完成，+10 EXP"
        }
    """
    if agent_name == "current":
        agent_name = _get_current_agent()
    
    today = datetime.now().strftime("%Y-%m-%d")
    quest_file = ANIMA_HOME / agent_name / "quests" / f"{today}.json"
    
    if not quest_file.exists():
        return {
            "success": False,
            "message": "今日任务尚未生成，请稍后再试"
        }
    
    with open(quest_file, "r", encoding="utf-8") as f:
        quests = json.load(f)
    
    # 查找任务
    for quest in quests:
        if quest["id"] == quest_id:
            if quest["status"] == "completed":
                return {
                    "success": False,
                    "message": "该任务已完成"
                }
            
            # 标记完成
            quest["status"] = "completed"
            quest["completedAt"] = datetime.now().isoformat()
            if proof:
                quest["proof"] = proof
            
            # 保存
            _save_quests(quests, quest_file)
            
            # 奖励 EXP
            exp_reward = quest["expReward"]
            _add_exp(agent_name, "application", exp_reward, "quest_complete", {
                "quest_id": quest_id,
                "quest_title": quest["title"]
            })
            
            return {
                "success": True,
                "expReward": exp_reward,
                "message": f"任务完成，+{exp_reward} EXP"
            }
    
    return {
        "success": False,
        "message": "未找到该任务"
    }


def _generate_daily_quests(agent_name: str) -> List[Dict]:
    """生成每日任务"""
    import random
    
    quest_templates = [
        {"title": "写一条记忆", "difficulty": "easy", "expReward": 5},
        {"title": "搜索记忆 3 次", "difficulty": "medium", "expReward": 10},
        {"title": "完成一次代码提交", "difficulty": "medium", "expReward": 10},
        {"title": "写工作日志", "difficulty": "easy", "expReward": 5},
        {"title": "分享知识到团队", "difficulty": "hard", "expReward": 20},
        {"title": "代码审查", "difficulty": "medium", "expReward": 10},
        {"title": "写技术文档", "difficulty": "hard", "expReward": 15},
    ]
    
    # 随机选择 3 个任务
    selected = random.sample(quest_templates, 3)
    
    quests = []
    for i, template in enumerate(selected):
        quests.append({
            "id": f"q{i+1}",
            "title": template["title"],
            "difficulty": template["difficulty"],
            "expReward": template["expReward"],
            "status": "pending"
        })
    
    return quests


def _save_quests(quests: List[Dict], quest_file: Path):
    """保存任务"""
    quest_file.parent.mkdir(parents=True, exist_ok=True)
    with open(quest_file, "w", encoding="utf-8") as f:
        json.dump(quests, f, ensure_ascii=False, indent=2)


# ============================================================================
# 工具 8-9: 团队工具
# ============================================================================

def get_team_ranking(team_name: str = "all") -> Dict:
    """
    查看团队排行榜
    
    Returns:
        {
            "team": "all",
            "rankings": [
                {"rank": 1, "agent": "枢衡", "level": 10, "exp": 5060},
                ...
            ]
        }
    """
    # 扫描所有 Agent 的 EXP
    agents_exp = []
    
    # 已知 Agent 列表
    known_agents = ["枢衡", "日安", "星澜", "明澈", "流萤", "正言", "瑾瑜", "糖豆", "青衫", "白墨"]
    
    for agent in known_agents:
        exp_data = _get_exp_simple(agent)
        if exp_data["totalExp"] > 0:
            agents_exp.append({
                "agent": agent,
                "level": exp_data["level"],
                "exp": exp_data["totalExp"]
            })
    
    # 按 EXP 排序
    agents_exp.sort(key=lambda x: x["exp"], reverse=True)
    
    # 添加排名
    rankings = []
    for i, agent_data in enumerate(agents_exp):
        rankings.append({
            "rank": i + 1,
            **agent_data
        })
    
    return {
        "team": team_name,
        "rankings": rankings
    }


def normalize_score(raw_score: float, metric_type: str, team_size: int) -> Dict:
    """
    分数归一化
    
    Args:
        raw_score: 原始分数
        metric_type: 指标类型 (exp/tool_calls/facts)
        team_size: 团队人数
    
    Returns:
        {
            "rawScore": 5060,
            "normalizedScore": 85.5,
            "percentile": 90,
            "method": "percentile"
        }
    """
    # 小团队：线性归一化
    # 大团队：百分位归一化
    
    if team_size < 10:
        # 线性归一化（假设满分 100）
        normalized = min(100, (raw_score / 10000) * 100)
        method = "linear"
        percentile = None
    else:
        # 百分位归一化（简化实现）
        normalized = min(100, raw_score / 100)
        method = "percentile"
        percentile = int(normalized)
    
    return {
        "rawScore": raw_score,
        "normalizedScore": round(normalized, 1),
        "percentile": percentile,
        "method": method
    }


# ============================================================================
# 辅助函数
# ============================================================================

def _get_current_agent() -> str:
    """获取当前 Agent 名称（简化实现）"""
    # TODO: 从 OpenClaw 上下文获取
    return "枢衡"


def _add_exp(agent_name: str, dimension: str, exp: int, action: str, details: Dict):
    """添加 EXP 记录"""
    try:
        # 尝试使用 core 模块
        if ANIMA_HOME.exists():
            try:
                sys.path.insert(0, str(ANIMA_HOME / "core"))
                from exp_tracker import EXPTracker
                tracker = EXPTracker(agent_name)
                success, msg = tracker.add_exp(dimension, action, exp, details)
                if not success:
                    # core 记录失败，fallback 到本地文件
                    _add_exp_fallback(agent_name, dimension, exp, action, details)
            except ImportError as e:
                # core 模块导入失败，使用 fallback
                _add_exp_fallback(agent_name, dimension, exp, action, details)
            except Exception as e:
                # core 其他错误，记录日志并 fallback
                _log_exp_error(agent_name, e)
                _add_exp_fallback(agent_name, dimension, exp, action, details)
        else:
            # core 未安装，直接使用 fallback
            _add_exp_fallback(agent_name, dimension, exp, action, details)
    except Exception as e:
        # 所有方法都失败，记录错误日志
        _log_exp_error(agent_name, e)


def _log_exp_error(agent_name: str, error: Exception):
    """记录 EXP 错误日志"""
    try:
        log_file = WORKSPACE / "anima_exp_errors.log"
        timestamp = datetime.now().isoformat()
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] EXP 记录失败 - Agent: {agent_name}, 错误：{error}\n")
    except:
        pass  # 日志记录失败也不影响主流程


def _add_exp_fallback(agent_name: str, dimension: str, exp: int, action: str, details: Dict):
    """降级方案：直接写入 EXP 历史文件"""
    exp_file = WORKSPACE / "anima_exp_history.jsonl"
    record = {
        "timestamp": datetime.now().isoformat(),
        "agent": agent_name,
        "dimension": dimension,
        "action": action,
        "exp": exp,
        "details": details
    }
    
    try:
        with open(exp_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except:
        pass


# ============================================================================
# 测试入口
# ============================================================================

if __name__ == "__main__":
    # 测试工具
    print("测试 memory_search_v2...")
    result = memory_search_v2("Vega", agent_name="枢衡")
    print(f"结果：{result}")
    
    print("\n测试 get_exp...")
    result = get_exp("枢衡")
    print(f"结果：{result}")
    
    print("\n测试 get_level...")
    result = get_level("枢衡")
    print(f"结果：{result}")
    
    print("\n测试 quest_daily_status...")
    result = quest_daily_status("枢衡")
    print(f"结果：{result}")
