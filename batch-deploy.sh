#!/bin/bash
# Memora v4.0 - 批量部署脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FACTS_BASE="/home/画像"

# 有效的 Agent 名称列表（中文名称，2 个字符以上）
VALID_AGENTS=(
    "乐言" "日安" "明澈" "星澜" "构稳" "枢衡" "检严" "正言"
    "流萤" "游策" "瑾瑜" "界安" "白墨" "立文" "糖豆" "维安" "青衫"
)

echo ""
echo "=========================================="
echo "  Memora v4.0 - 批量部署向导"
echo "=========================================="
echo ""

# 统计
TOTAL=0
SUCCESS=0
FAILED=0

# 遍历有效 Agent
for AGENT_NAME in "${VALID_AGENTS[@]}"; do
    AGENT_DIR="$FACTS_BASE/$AGENT_NAME"
    
    # 检查目录是否存在
    if [ ! -d "$AGENT_DIR" ]; then
        echo "⚠️  跳过 $AGENT_NAME（目录不存在）"
        continue
    fi
    
    TOTAL=$((TOTAL + 1))
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "部署 Agent: $AGENT_NAME"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # 确保目录结构
    mkdir -p "$AGENT_DIR/facts/episodic"
    mkdir -p "$AGENT_DIR/facts/semantic"
    mkdir -p "$AGENT_DIR/daily_quests"
    
    # 复制配置文件
    CONFIG_TEMPLATE="$SCRIPT_DIR/config/memora_config.template.json"
    AGENT_CONFIG="$AGENT_DIR/memora_config.json"
    
    if [ -f "$CONFIG_TEMPLATE" ]; then
        sed "s/{AGENT_NAME}/$AGENT_NAME/g" "$CONFIG_TEMPLATE" > "$AGENT_CONFIG"
        echo "✅ 配置文件已创建"
    fi
    
    # 生成认知画像
    cd "$SCRIPT_DIR/core"
    if python3 -c "
import sys
sys.path.insert(0, '.')
from cognitive_profile import CognitiveProfileGenerator

try:
    gen = CognitiveProfileGenerator('$AGENT_NAME')
    output_path = gen.save_profile()
    print('✅ 认知画像已生成')
except Exception as e:
    print(f'⚠️  认知画像生成失败：{e}')
    sys.exit(1)
" 2>&1; then
        SUCCESS=$((SUCCESS + 1))
        echo "✅ $AGENT_NAME 部署成功"
    else
        FAILED=$((FAILED + 1))
        echo "❌ $AGENT_NAME 部署失败"
    fi
done

# 总结
echo ""
echo "=========================================="
echo "  批量部署完成！"
echo "=========================================="
echo ""
echo "📊 统计:"
echo "   总计尝试：$TOTAL"
echo "   ✅ 成功：$SUCCESS"
echo "   ❌ 失败：$FAILED"
echo ""

if [ $FAILED -eq 0 ]; then
    echo "🎉 所有 Agent 部署成功！"
else
    echo "⚠️  有 $FAILED 个 Agent 部署失败"
fi

echo ""
echo "📚 下一步:"
echo ""
echo "1. 查看所有 Agent 的认知进度:"
echo "   cd $SCRIPT_DIR"
echo "   python3 demo.py <Agent 名称>"
echo ""
echo "2. 查看团队扫描结果:"
echo "   cd core"
echo "   python3 team_scanner.py"
echo ""
echo "3. 生成团队对比卡片:"
echo "   python3 profile_card.py comparison"
echo ""
echo "=========================================="
echo ""
