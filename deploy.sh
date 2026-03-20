#!/bin/bash
# Memora v4.0 - 部署脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_NAME="${1:-}"

echo ""
echo "=========================================="
echo "  Memora v4.0 - 部署向导"
echo "=========================================="
echo ""

# 检查 Python 版本
echo "📋 检查环境..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Python 版本：$PYTHON_VERSION"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 9) else 1)"; then
    echo "   ❌ Python 版本过低，需要 3.9+"
    exit 1
fi
echo "   ✅ Python 版本符合要求"
echo ""

# 检查 Agent 名称
if [ -z "$AGENT_NAME" ]; then
    echo "用法：$0 <Agent 名称>"
    echo ""
    echo "可用 Agent:"
    ls /home/画像/ | grep -v "^\." | grep -v "shared" | head -10
    echo ""
    exit 1
fi

AGENT_DIR="/home/画像/$AGENT_NAME"

# 检查 Agent 目录
if [ ! -d "$AGENT_DIR" ]; then
    echo "⚠️  Agent 目录不存在：$AGENT_DIR"
    echo "   是否创建？(y/N)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        mkdir -p "$AGENT_DIR"
        mkdir -p "$AGENT_DIR/facts/episodic"
        mkdir -p "$AGENT_DIR/facts/semantic"
        echo "   ✅ 已创建 Agent 目录结构"
    else
        echo "   ❌ 部署已取消"
        exit 1
    fi
else
    echo "✅ Agent 目录存在：$AGENT_DIR"
fi

# 确保 facts 目录结构
echo ""
echo "📁 检查目录结构..."
mkdir -p "$AGENT_DIR/facts/episodic"
mkdir -p "$AGENT_DIR/facts/semantic"
mkdir -p "$AGENT_DIR/daily_quests"
echo "   ✅ 目录结构就绪"

# 复制配置模板
echo ""
echo "📋 复制配置文件..."
CONFIG_TEMPLATE="$SCRIPT_DIR/config/memora_config.template.json"
AGENT_CONFIG="$AGENT_DIR/memora_config.json"

if [ -f "$CONFIG_TEMPLATE" ]; then
    # 替换 Agent 名称
    sed "s/{AGENT_NAME}/$AGENT_NAME/g" "$CONFIG_TEMPLATE" > "$AGENT_CONFIG"
    echo "   ✅ 配置文件已创建：$AGENT_CONFIG"
else
    echo "   ⚠️  配置模板不存在，跳过"
fi

# 运行测试
echo ""
echo "🧪 运行快速测试..."
cd "$SCRIPT_DIR/core"
if python3 -c "
import sys
sys.path.insert(0, '.')
from team_scanner import TeamScanner
from cognitive_profile import CognitiveProfileGenerator

scanner = TeamScanner()
agents = scanner.scan_active_agents()
print(f'   检测到 {len(agents)} 个活跃 Agent')

gen = CognitiveProfileGenerator('$AGENT_NAME')
profile = gen.generate_profile(auto_scan=True)
print(f'   ✅ 认知画像生成成功')
print(f'   等级：Lv.{profile.get(\"level\", 0)}')
print(f'   分数：{profile.get(\"cognitive_score\", 0):.1f}')
" 2>&1; then
    echo "   ✅ 测试通过"
else
    echo "   ⚠️  测试失败，但继续部署"
fi

# 生成初始认知画像
echo ""
echo "📊 生成初始认知画像..."
cd "$SCRIPT_DIR/core"
python3 -c "
import sys
sys.path.insert(0, '.')
from cognitive_profile import CognitiveProfileGenerator

gen = CognitiveProfileGenerator('$AGENT_NAME')
output_path = gen.save_profile()
print(f'   ✅ 已保存到：{output_path}')
"

# 配置 Cron（可选）
echo ""
echo "⏰ 配置 Cron 任务..."
echo ""
echo "   是否配置自动任务刷新和检查？(y/N)"
read -r response

if [[ "$response" =~ ^[Yy]$ ]]; then
    CRON_FILE="$SCRIPT_DIR/cron/memora-v4-crontab"
    if [ -f "$CRON_FILE" ]; then
        # 替换 Agent 名称和路径
        TEMP_CRON=$(mktemp)
        sed "s/AGENT_NAME=\".*\"/AGENT_NAME=\"$AGENT_NAME\"/" "$CRON_FILE" | \
        sed "s|MEMORA_DIR=\".*\"|MEMORA_DIR=\"$SCRIPT_DIR\"|" > "$TEMP_CRON"
        
        # 安装 Cron（覆盖方式，避免追加错误）
        crontab "$TEMP_CRON"
        rm -f "$TEMP_CRON"
        
        echo "   ✅ Cron 任务已配置"
        echo ""
        echo "   已配置的任务："
        echo "   - 05:00 刷新每日任务"
        echo "   - 每小时检查任务进度"
        echo "   - 06:00 生成认知画像"
    else
        echo "   ⚠️  Cron 配置文件不存在"
    fi
else
    echo "   跳过 Cron 配置"
fi

# 完成
echo ""
echo "=========================================="
echo "  ✅ $AGENT_NAME 部署完成！"
echo "=========================================="
echo ""
echo "📚 下一步："
echo ""
echo "1. 查看认知进度:"
echo "   cd $SCRIPT_DIR"
echo "   ./scripts/show-progress.sh $AGENT_NAME"
echo ""
echo "2. 刷新每日任务:"
echo "   ./scripts/refresh-quests.sh $AGENT_NAME"
echo ""
echo "3. 查看任务状态:"
echo "   cd core"
echo "   python3 daily_quest.py $AGENT_NAME status"
echo ""
echo "4. 查看完整画像:"
echo "   python3 demo.py $AGENT_NAME"
echo ""
echo "=========================================="
echo ""
