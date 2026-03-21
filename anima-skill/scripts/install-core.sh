#!/bin/bash
# Anima-AIOS Core 独立安装脚本
# 可单独运行，也可被 post-install.sh 调用

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ANIMA_HOME="$HOME/.anima"

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}📦 正在安装 Anima-AIOS core...${NC}"

# 检查是否已安装
if [ -d "$ANIMA_HOME" ]; then
    echo -e "${YELLOW}⚠️  $ANIMA_HOME 已存在${NC}"
    read -p "是否覆盖安装？(y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "取消安装"
        exit 0
    fi
    rm -rf "$ANIMA_HOME"
fi

# 创建临时目录
TEMP_DIR="/tmp/anima-core-install-$$"
mkdir -p "$TEMP_DIR"

# 克隆仓库
echo "   → 克隆仓库..."
git clone --depth 1 --quiet https://github.com/anima-aios/anima.git "$TEMP_DIR"

# 运行主安装脚本
echo "   → 执行安装..."
bash "$TEMP_DIR/install.sh"

# 清理
rm -rf "$TEMP_DIR"

echo -e "${GREEN}✅ Anima-AIOS core 安装完成！${NC}"
echo ""
echo "数据目录：$ANIMA_HOME"
echo "核心模块：$ANIMA_HOME/core/"
