#!/bin/bash
# Anima-AIOS Skill - Post Install Script
# 自动安装 Anima-AIOS core 核心系统

set -e

echo "🚀 ════════════════════════════════════════════"
echo "🚀       正在安装 Anima-AIOS 认知操作系统"
echo "🚀 ════════════════════════════════════════════"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查 Python
echo -e "${BLUE}[1/5]${NC} 检查 Python 环境..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ 错误：需要 Python 3${NC}"
    echo "请安装 Python 3.8+ 后重试"
    exit 1
fi
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✅ Python ${PYTHON_VERSION} 已安装${NC}"

# 检查 Git
echo -e "${BLUE}[2/5]${NC} 检查 Git..."
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ 错误：需要 Git${NC}"
    echo "请安装 Git 后重试"
    exit 1
fi
GIT_VERSION=$(git --version | cut -d' ' -f3)
echo -e "${GREEN}✅ Git ${GIT_VERSION} 已安装${NC}"

# 检查并安装 core
echo -e "${BLUE}[3/5]${NC} 检查 Anima-AIOS core..."
ANIMA_HOME="$HOME/.anima"

if [ -d "$ANIMA_HOME" ]; then
    echo -e "${GREEN}✅ Anima-AIOS core 已安装，跳过${NC}"
else
    echo -e "${YELLOW}📦 未检测到 core，正在安装...${NC}"
    
    # 创建临时目录
    TEMP_DIR="/tmp/anima-install-$$"
    mkdir -p "$TEMP_DIR"
    
    # 克隆仓库（只克隆最新 commit，加快速度）
    echo "   → 克隆仓库..."
    git clone --depth 1 --quiet https://github.com/anima-aios/anima.git "$TEMP_DIR"
    
    # 运行安装脚本
    echo "   → 执行安装脚本..."
    bash "$TEMP_DIR/install.sh" --quiet
    
    # 清理临时目录
    rm -rf "$TEMP_DIR"
    
    echo -e "${GREEN}✅ Anima-AIOS core 安装完成${NC}"
fi

# 安装 Python 依赖
echo -e "${BLUE}[4/5]${NC} 安装 Python 依赖..."
pip3 install pytest requests --quiet --user 2>/dev/null || {
    echo -e "${YELLOW}⚠️  pytest 安装失败（可选），不影响核心功能${NC}"
}
echo -e "${GREEN}✅ Python 依赖安装完成${NC}"

# 验证安装
echo -e "${BLUE}[5/5]${NC} 验证安装..."
if [ -f "$ANIMA_HOME/core/exp_tracker.py" ]; then
    echo -e "${GREEN}✅ 核心文件验证通过${NC}"
else
    echo -e "${RED}❌ 核心文件缺失，安装可能失败${NC}"
    exit 1
fi

echo ""
echo "🎉 ════════════════════════════════════════════"
echo "🎉          Anima-AIOS 安装完成！"
echo "🎉 ════════════════════════════════════════════"
echo ""
echo -e "${GREEN}✨ 现在可以使用以下功能：${NC}"
echo ""
echo "   📊 认知画像"
echo "      '我的认知画像是什么？'"
echo ""
echo "   📈 经验值查询"
echo "      '我的经验值是多少？'"
echo "      '我现在的等级是多少？'"
echo ""
echo "   🎮 每日任务"
echo "      '今天的任务是什么？'"
echo "      '完成任务：写周报'"
echo ""
echo "   🔍 智能记忆"
echo "      '搜索关于 Vega 的记忆'"
echo "      '记住：今天完成了 Anima v5.0 发布'"
echo ""
echo "   📊 团队排行"
echo "      '查看团队 EXP 排行榜'"
echo ""
echo -e "${YELLOW}📚 更多文档：https://github.com/anima-aios/anima${NC}"
echo ""
