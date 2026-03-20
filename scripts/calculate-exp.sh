#!/bin/bash
# Memora v4.0 - 计算 EXP
# 用法：./calculate-exp.sh <Agent 名称> [开始日期] [结束日期]

set -e

AGENT_NAME="${1:-}"
START_DATE="${2:-}"
END_DATE="${3:-$(date +%Y-%m-%d)}"

if [ -z "$AGENT_NAME" ]; then
    echo "用法：$0 <Agent 名称> [开始日期] [结束日期]"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CORE_DIR="$SCRIPT_DIR/../core"

cd "$CORE_DIR"

echo ""
echo "=== 📊 $AGENT_NAME 的 EXP 统计 ==="
echo ""

# 创建临时 Python 脚本
cat > /tmp/calc_exp_$$.py << 'PYTHON_SCRIPT'
import sys
import json
from pathlib import Path

agent_name = sys.argv[1]
start_date = sys.argv[2] if len(sys.argv) > 2 else None
end_date = sys.argv[3] if len(sys.argv) > 3 else None

facts_base = Path('/home/画像')
agent_dir = facts_base / agent_name
exp_history_file = agent_dir / 'exp_history.jsonl'

if not exp_history_file.exists():
    print("❌ 未找到 EXP 历史记录")
    sys.exit(1)

# 统计
total_exp = 0.0
dimension_exp = {}
daily_exp = {}

with open(exp_history_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            record = json.loads(line.strip())
            record_date = record.get('date', '')
            
            # 过滤日期
            if start_date and record_date < start_date:
                continue
            if end_date and record_date > end_date:
                continue
            
            exp = record.get('exp', 0)
            dimension = record.get('dimension', 'unknown')
            
            total_exp += exp
            
            if dimension not in dimension_exp:
                dimension_exp[dimension] = 0.0
            dimension_exp[dimension] += exp
            
            if record_date not in daily_exp:
                daily_exp[record_date] = 0.0
            daily_exp[record_date] += exp
        except:
            continue

# 输出
print(f"统计周期：{start_date or '开始'} ~ {end_date or '今天'}")
print(f"总 EXP: {total_exp:.1f}")
print("")
print("各维度:")
for dim, exp in sorted(dimension_exp.items(), key=lambda x: -x[1]):
    print(f"  {dim:20s}: {exp:6.1f} EXP")

print("")
print("每日趋势（最近 7 天）:")
sorted_dates = sorted(daily_exp.keys())[-7:]
for date in sorted_dates:
    print(f"  {date}: {daily_exp[date]:.1f} EXP")

PYTHON_SCRIPT

python3 /tmp/calc_exp_$$.py "$AGENT_NAME" "$START_DATE" "$END_DATE"

# 清理
rm -f /tmp/calc_exp_$$.py

echo ""
