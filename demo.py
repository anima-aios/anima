#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Memora v4.0 - 演示脚本

展示完整的认知画像生成流程

用法：python3 demo.py [Agent 名称]
"""

import sys
from pathlib import Path

# 添加核心模块路径
sys.path.insert(0, str(Path(__file__).parent / 'core'))

from team_scanner import TeamScanner
from cognitive_profile import CognitiveProfileGenerator
from profile_card import ProfileCardGenerator


def main():
    agent_name = sys.argv[1] if len(sys.argv) > 1 else '枢衡'
    
    print("\n")
    print("=" * 60)
    print("  Memora v4.0 Phase 6 — 认知画像演示")
    print("=" * 60)
    print()
    
    # 1. 团队扫描
    print("📡 步骤 1: 扫描活跃 Agent...")
    print("-" * 60)
    scanner = TeamScanner()
    active_agents = scanner.scan_active_agents()
    
    if active_agents:
        print(f"✅ 检测到 {len(active_agents)} 个活跃 Agent:")
        for agent in active_agents:
            print(f"   - {agent}")
    else:
        print("⚠️  未检测到活跃 Agent")
    print()
    
    # 2. 生成认知画像
    print(f"🧠 步骤 2: 生成 {agent_name} 的认知画像...")
    print("-" * 60)
    generator = CognitiveProfileGenerator(agent_name)
    profile = generator.generate_profile(auto_scan=True)
    print(f"✅ 认知画像生成完成")
    print(f"   团队规模：{len(active_agents)}")
    print(f"   归一化模式：自动检测")
    print()
    
    # 3. 生成完整卡片
    print("📊 步骤 3: 生成完整认知画像卡片...")
    print("-" * 60)
    card_gen = ProfileCardGenerator()
    full_card = card_gen.generate_card(profile)
    print(full_card)
    print()
    
    # 4. 生成简化版
    print("📝 步骤 4: 生成简化版卡片（适合每日查看）...")
    print("-" * 60)
    simple_card = card_gen.generate_simple_card(profile)
    print(simple_card)
    print()
    
    # 5. 团队对比（如果有多个 Agent）
    if len(active_agents) > 1:
        print("🏆 步骤 5: 生成团队对比卡片...")
        print("-" * 60)
        
        profiles = []
        for agent in active_agents:
            try:
                gen = CognitiveProfileGenerator(agent)
                profiles.append(gen.generate_profile(auto_scan=False))
            except Exception as e:
                print(f"⚠️  无法生成 {agent} 的画像：{e}")
        
        if profiles:
            comparison_card = card_gen.generate_comparison_card(profiles)
            print(comparison_card)
        print()
    
    # 6. 保存结果
    print("💾 步骤 6: 保存认知画像...")
    print("-" * 60)
    output_path = generator.save_profile()
    print(f"✅ 已保存到：{output_path}")
    print()
    
    # 完成
    print("=" * 60)
    print("  ✅ 演示完成！")
    print("=" * 60)
    print()
    print("📚 下一步:")
    print()
    print("1. 查看完整文档:")
    print(f"   cat {Path(__file__).parent}/README.md")
    print()
    print("2. 每日查看认知进度:")
    print(f"   ./scripts/show-progress.sh {agent_name}")
    print()
    print("3. 刷新每日任务:")
    print(f"   ./scripts/refresh-quests.sh {agent_name}")
    print()
    print()


if __name__ == '__main__':
    main()
