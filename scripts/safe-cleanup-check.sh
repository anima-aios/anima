#!/bin/bash
# Memora v4.0 - 安全清理检查脚本
# 在删除任何数据前必须运行此脚本

set -e

TARGET_DIR="${1:-}"

echo ""
echo "=========================================="
echo "  ⚠️  Memora v4.0 - 安全清理检查"
echo "=========================================="
echo ""

if [ -z "$TARGET_DIR" ]; then
    echo "❌ 错误：请指定要清理的目录"
    echo ""
    echo "用法：$0 <要清理的目录>"
    echo ""
    echo "示例："
    echo "   $0 /home/画像/枢衡/facts"
    echo ""
    exit 1
fi

# 检查是否是 Memora 数据目录
if [[ ! "$TARGET_DIR" == *"/画像/"* ]]; then
    echo "❌ 错误：这不是 Memora 数据目录"
    echo "   目录：$TARGET_DIR"
    echo ""
    exit 1
fi

# 检查是否存在
if [ ! -d "$TARGET_DIR" ]; then
    echo "❌ 错误：目录不存在"
    echo "   目录：$TARGET_DIR"
    echo ""
    exit 1
fi

# 检查保护标记
if [ -f "$TARGET_DIR/../DO_NOT_DELETE.txt" ] || [ -f "$TARGET_DIR/DO_NOT_DELETE.txt" ]; then
    echo "⚠️  警告：检测到保护标记！"
    echo ""
    echo "   此目录受 Memora v4.0 保护。"
    echo ""
    echo "   删除前请确认："
    echo "   1. 已备份数据"
    echo "   2. 已获得枢衡授权"
    echo "   3. 确认真的需要删除"
    echo ""
    cat "$TARGET_DIR/../DO_NOT_DELETE.txt" 2>/dev/null || cat "$TARGET_DIR/DO_NOT_DELETE.txt" 2>/dev/null || true
    echo ""
    
    echo "⚠️  是否继续删除？(YES/NO)"
    read -r response
    
    if [[ "$response" != "YES" ]]; then
        echo ""
        echo "❌ 已取消删除操作"
        echo ""
        exit 0
    fi
fi

# 检查是否有备份
BACKUP_BASE="/home/画像/.backup"
if [ -d "$BACKUP_BASE" ]; then
    latest_backup=$(ls -t "$BACKUP_BASE/facts/" 2>/dev/null | head -1)
    if [ -n "$latest_backup" ]; then
        echo "✅ 检测到备份"
        echo "   最新备份：$latest_backup"
        echo ""
    else
        echo "⚠️  警告：未检测到备份！"
        echo ""
        echo "   建议先运行备份："
        echo "   ./scripts/protect-data.sh"
        echo ""
        
        echo "⚠️  是否先备份？(y/N)"
        read -r response
        
        if [[ "$response" =~ ^[Yy]$ ]]; then
            echo ""
            echo "🚀 运行备份..."
            ./scripts/protect-data.sh
        fi
    fi
else
    echo "⚠️  警告：备份目录不存在！"
    echo ""
    echo "   建议先创建备份目录并备份数据"
    echo ""
fi

# 统计要删除的数据
echo "📊 待删除数据统计"
file_count=$(find "$TARGET_DIR" -type f 2>/dev/null | wc -l)
dir_size=$(du -sh "$TARGET_DIR" 2>/dev/null | cut -f1)
echo "   文件数量：$file_count"
echo "   目录大小：$dir_size"
echo ""

# 最终确认
echo "⚠️  最终确认"
echo ""
echo "   即将删除：$TARGET_DIR"
echo "   文件数量：$file_count"
echo "   目录大小：$dir_size"
echo ""
echo "   此操作不可恢复！"
echo ""
echo "   请输入\"DELETE\"确认删除："
read -r confirmation

if [[ "$confirmation" == "DELETE" ]]; then
    echo ""
    echo "✅ 确认删除"
    echo ""
    echo "   请手动执行删除命令："
    echo "   rm -rf $TARGET_DIR"
    echo ""
    exit 0
else
    echo ""
    echo "❌ 已取消删除操作"
    echo ""
    exit 0
fi
