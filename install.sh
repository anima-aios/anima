#!/bin/bash
# Anima-AIOS v5.0 - 安装脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_NAME="${1:-}"

echo ""
echo "=========================================="
echo "  Anima-AIOS v5.0 - 安装向导"
echo "=========================================="
echo ""

# 检查 Python 版本
echo "📋 检查 Python 版本..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Python 版本：$PYTHON_VERSION"

# 检查是否 >= 3.9
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 9) else 1)"; then
    echo "   ❌ Python 版本过低，需要 3.9+"
    exit 1
fi
echo "   ✅ Python 版本符合要求"
echo ""

# 检查 Agent 名称
if [ -z "$AGENT_NAME" ]; then
    echo "⚠️  未提供 Agent 名称，使用示例配置"
    echo ""
    echo "用法：$0 <Agent 名称>"
    echo "例如：$0 枢衡"
    echo ""
    echo "继续安装基础框架...（不配置具体 Agent）"
    echo ""
else
    echo "👤 Agent 名称：$AGENT_NAME"
    echo ""
    
    # 检查 Agent 目录
    AGENT_DIR="/home/画像/$AGENT_NAME"
    if [ ! -d "$AGENT_DIR" ]; then
        echo "⚠️  Agent 目录不存在：$AGENT_DIR"
        echo "   将自动创建..."
        mkdir -p "$AGENT_DIR"
    fi
    echo "   ✅ Agent 目录就绪"
    
    # 复制配置模板
    echo ""
    echo "📋 复制配置模板..."
    
    CONFIG_TEMPLATE="$SCRIPT_DIR/config/memora_config.template.json"
    AGENT_CONFIG="$AGENT_DIR/memora_config.json"
    
    if [ -f "$CONFIG_TEMPLATE" ]; then
        cp "$CONFIG_TEMPLATE" "$AGENT_CONFIG"
        echo "   ✅ 配置文件已创建：$AGENT_CONFIG"
    else
        echo "   ⚠️  配置模板不存在，跳过"
    fi
fi

# 运行测试
echo ""
echo "🧪 运行测试套件..."
cd "$SCRIPT_DIR/openclaw-plugin"
if python3 -m pytest tests/ -q > /tmp/memora_install_test.log 2>&1; then
    echo "   ✅ 所有测试通过"
else
    echo "   ⚠️  部分测试失败，查看详细日志："
    cat /tmp/memora_install_test.log
    echo ""
    echo "   是否继续安装？(y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "   安装已取消"
        exit 1
    fi
fi
rm -f /tmp/memora_install_test.log

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
        
        # 安装 Cron
        crontab "$TEMP_CRON"
        rm -f "$TEMP_CRON"
        
        echo "   ✅ Cron 任务已配置"
        echo ""
        echo "   已配置的任务："
        echo "   - 05:00 刷新每日任务"
        echo "   - 每小时检查任务进度"
        echo "   - 06:00 生成认知画像"
        echo "   - 每周日 23:00 生成 EXP 统计"
    else
        echo "   ⚠️  Cron 配置文件不存在"
    fi
else
    echo "   跳过 Cron 配置"
fi

# 创建日志目录
echo ""
echo "📁 创建日志目录..."
LOG_DIR="/var/log/memora-v4"
if [ ! -d "$LOG_DIR" ]; then
    sudo mkdir -p "$LOG_DIR" 2>/dev/null || mkdir -p "$LOG_DIR"
fi
echo "   ✅ 日志目录：$LOG_DIR"

# 完成
echo ""
echo "=========================================="
echo "  ✅ 安装完成！"
echo "=========================================="
echo ""
echo "📚 下一步："
echo ""
echo "1. 查看认知进度："
echo "   cd $SCRIPT_DIR"
echo "   ./scripts/show-progress.sh $AGENT_NAME"
echo ""
echo "2. 刷新每日任务："
echo "   ./scripts/refresh-quests.sh $AGENT_NAME"
echo ""
echo "3. 查看任务状态："
echo "   cd core"
echo "   python3 daily_quest.py $AGENT_NAME status"
echo ""
echo "4. 配置 OpenClaw 插件（可选）："
echo "   编辑 ~/.openclaw/openclaw.json"
echo "   添加 Memora v4 插件配置"
echo ""
echo "=========================================="
echo ""
