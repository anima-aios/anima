#!/bin/bash
# Memora v4.0 Phase 5 - 运行所有测试

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEST_DIR="$SCRIPT_DIR"

echo ""
echo "=========================================="
echo "  Memora v4.0 Phase 5 - 测试套件"
echo "=========================================="
echo ""

# 计数器
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# 测试 1: 归一化引擎
echo "🧪 测试 1: 归一化引擎..."
cd "$TEST_DIR"
if python3 test_normalization.py > /tmp/test_normalization.log 2>&1; then
    echo "   ✅ 归一化引擎测试通过"
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "   ❌ 归一化引擎测试失败"
    cat /tmp/test_normalization.log
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi
TOTAL_TESTS=$((TOTAL_TESTS + 1))

# 测试 2: EXP 追踪器
echo "🧪 测试 2: EXP 追踪器..."
if python3 test_exp_tracker.py > /tmp/test_exp_tracker.log 2>&1; then
    echo "   ✅ EXP 追踪器测试通过"
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "   ❌ EXP 追踪器测试失败"
    cat /tmp/test_exp_tracker.log
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi
TOTAL_TESTS=$((TOTAL_TESTS + 1))

# 测试 3: 每日任务系统
echo "🧪 测试 3: 每日任务系统..."
if python3 test_daily_quest.py > /tmp/test_daily_quest.log 2>&1; then
    echo "   ✅ 每日任务系统测试通过"
    PASSED_TESTS=$((PASSED_TESTS + 1))
else
    echo "   ❌ 每日任务系统测试失败"
    cat /tmp/test_daily_quest.log
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi
TOTAL_TESTS=$((TOTAL_TESTS + 1))

# 清理日志
rm -f /tmp/test_*.log

# 总结
echo ""
echo "=========================================="
echo "  测试结果汇总"
echo "=========================================="
echo "  总测试数：$TOTAL_TESTS"
echo "  ✅ 通过：$PASSED_TESTS"
echo "  ❌ 失败：$FAILED_TESTS"
echo "=========================================="
echo ""

if [ $FAILED_TESTS -eq 0 ]; then
    echo "🎉 所有测试通过！"
    exit 0
else
    echo "⚠️  有 $FAILED_TESTS 个测试失败"
    exit 1
fi
