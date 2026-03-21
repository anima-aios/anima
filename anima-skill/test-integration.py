#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anima-AIOS v5.0 - 完整集成测试

测试范围：
1. skill 模块导入
2. core 模块集成（如果已安装）
3. 记忆工具（memory_search_v2, memory_write_v2）
4. 认知工具（get_cognitive_profile, get_exp, get_level）
5. 任务工具（quest_daily_status, quest_complete）
6. 团队工具（get_team_ranking）
7. 数据持久化
8. 降级模式

运行：
python3 test-integration.py
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# 颜色定义
class Colors:
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color

def print_header(text):
    print(f"\n{Colors.BLUE}{'=' * 60}{Colors.NC}")
    print(f"{Colors.BLUE}{text}{Colors.NC}")
    print(f"{Colors.BLUE}{'=' * 60}{Colors.NC}")

def print_success(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.NC}")

def print_error(text):
    print(f"{Colors.RED}❌ {text}{Colors.NC}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.NC}")

def print_info(text):
    print(f"   {text}")

# 测试计数器
tests_passed = 0
tests_failed = 0

def test(name, func):
    global tests_passed, tests_failed
    try:
        func()
        print_success(name)
        tests_passed += 1
    except Exception as e:
        print_error(f"{name}: {e}")
        tests_failed += 1

# ============================================================================
# 测试用例
# ============================================================================

def test_skill_import():
    """测试 1: skill 模块导入"""
    from anima_tools import (
        memory_search_v2,
        memory_write_v2,
        get_cognitive_profile,
        get_exp,
        get_level,
        quest_daily_status,
        quest_complete,
        get_team_ranking
    )
    print_info("所有工具导入成功")

def test_core_detection():
    """测试 2: core 检测"""
    from anima_tools import ANIMA_HOME
    if ANIMA_HOME.exists():
        print_info(f"core 已安装：{ANIMA_HOME}")
        core_files = list((ANIMA_HOME / "core").glob("*.py"))
        print_info(f"核心模块：{len(core_files)} 个文件")
    else:
        print_warning("core 未安装，使用降级模式")

def test_memory_write():
    """测试 3: 记忆写入"""
    from anima_tools import memory_write_v2
    result = memory_write_v2(
        content=f"测试：集成测试记录 {datetime.now().strftime('%H:%M:%S')}",
        type="episodic",
        agent_name="枢衡"
    )
    print_info(f"结果：{result['message']}")
    print_info(f"EXP 奖励：+{result['expReward']}")
    assert 'factId' in result

def test_memory_search():
    """测试 4: 记忆搜索"""
    from anima_tools import memory_search_v2
    result = memory_search_v2(
        query="测试",
        type="all",
        maxResults=5,
        agent_name="枢衡"
    )
    print_info(f"找到 {result['count']} 条记忆")
    print_info(f"EXP 奖励：+{result['expReward']}")
    assert 'results' in result

def test_get_exp():
    """测试 5: EXP 查询"""
    from anima_tools import get_exp
    result = get_exp("枢衡")
    print_info(f"总 EXP: {result['totalExp']}")
    print_info(f"今日 EXP: {result['todayExp']}")
    print_info(f"等级：Lv.{result['level']}")
    assert 'totalExp' in result
    assert 'level' in result

def test_get_level():
    """测试 6: 等级查询"""
    from anima_tools import get_level
    result = get_level("枢衡")
    print_info(f"当前等级：Lv.{result['currentLevel']}")
    print_info(f"进度：{result['progressBar']}")
    assert 'currentLevel' in result
    assert 'progressBar' in result

def test_get_cognitive_profile():
    """测试 7: 认知画像"""
    from anima_tools import get_cognitive_profile
    result = get_cognitive_profile("枢衡")
    print_info(f"Agent: {result['agent']}")
    print_info(f"等级：Lv.{result['level']}")
    print_info(f"EXP: {result['exp']}")
    if result['dimensions']:
        print_info(f"维度：{len(result['dimensions'])} 个")
    assert 'agent' in result
    assert 'level' in result

def test_quest_daily_status():
    """测试 8: 每日任务状态"""
    from anima_tools import quest_daily_status
    result = quest_daily_status("枢衡")
    print_info(f"今日任务数：{len(result['quests'])}")
    for q in result['quests']:
        print_info(f"  - {q['title']} ({q['difficulty']}) +{q['expReward']} EXP")
    assert 'quests' in result
    assert 'date' in result

def test_quest_complete():
    """测试 9: 任务完成"""
    from anima_tools import quest_daily_status, quest_complete
    quests = quest_daily_status("枢衡")
    if quests['quests']:
        # 找一个未完成的任务
        for quest in quests['quests']:
            if quest['status'] == 'pending':
                result = quest_complete(quest['id'], proof="测试完成", agent_name="枢衡")
                print_info(f"任务：{quest['title']}")
                print_info(f"结果：{result['message']}")
                assert result['success']
                return
        print_warning("所有任务已完成")
    else:
        print_warning("无可用任务")

def test_team_ranking():
    """测试 10: 团队排行"""
    from anima_tools import get_team_ranking
    result = get_team_ranking()
    print_info(f"团队人数：{len(result['rankings'])}")
    for r in result['rankings'][:3]:
        print_info(f"  #{r['rank']} {r['agent']} Lv.{r['level']} {r['exp']} EXP")
    assert 'rankings' in result

def test_data_persistence():
    """测试 11: 数据持久化"""
    from anima_tools import WORKSPACE
    data_files = [
        WORKSPACE / "anima_exp_history.jsonl",
    ]
    for f in data_files:
        if f.exists():
            size = f.stat().st_size
            print_info(f"✅ {f.name} ({size} 字节)")
        else:
            print_warning(f"{f.name} 不存在")

def test_degradation_mode():
    """测试 12: 降级模式"""
    from anima_tools import ANIMA_HOME
    # 检查 core 是否存在
    core_exists = ANIMA_HOME.exists() and (ANIMA_HOME / "core").exists()
    
    if not core_exists:
        print_warning("core 未安装，验证降级模式...")
        from anima_tools import get_cognitive_profile
        result = get_cognitive_profile("枢衡")
        if "core 未安装" in result.get("progress", "") or "安装 core" in result.get("radar", ""):
            print_info("降级模式正常工作")
        else:
            print_warning("降级模式提示缺失")
    else:
        print_info("core 已安装，跳过降级测试")

# ============================================================================
# 主测试流程
# ============================================================================

def main():
    print_header("Anima-AIOS v5.0 - 完整集成测试")
    print_info(f"测试时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print_info(f"Python 版本：{sys.version.split()[0]}")
    print_info(f"工作目录：{Path.cwd()}")
    
    print_header("测试开始")
    
    # 运行所有测试
    test("skill 模块导入", test_skill_import)
    test("core 检测", test_core_detection)
    test("记忆写入", test_memory_write)
    test("记忆搜索", test_memory_search)
    test("EXP 查询", test_get_exp)
    test("等级查询", test_get_level)
    test("认知画像", test_get_cognitive_profile)
    test("每日任务状态", test_quest_daily_status)
    test("任务完成", test_quest_complete)
    test("团队排行", test_team_ranking)
    test("数据持久化", test_data_persistence)
    test("降级模式", test_degradation_mode)
    
    # 测试总结
    print_header("测试总结")
    print_info(f"通过：{tests_passed} 个")
    print_info(f"失败：{tests_failed} 个")
    
    if tests_failed == 0:
        print_success("所有测试通过！✅")
        return 0
    else:
        print_error(f"{tests_failed} 个测试失败 ❌")
        return 1

if __name__ == "__main__":
    sys.exit(main())
