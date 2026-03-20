#!/bin/bash
# Memora v4.0 - 数据保护脚本

set -e

FACTS_BASE="/home/画像"
BACKUP_BASE="/home/画像/.backup"
DATE=$(date +%Y%m%d_%H%M%S)

echo ""
echo "=========================================="
echo "  Memora v4.0 - 数据保护检查"
echo "=========================================="
echo ""

# 创建备份目录
echo "📁 创建备份目录..."
mkdir -p "$BACKUP_BASE/facts"
mkdir -p "$BACKUP_BASE/profiles"
echo "   ✅ 备份目录：$BACKUP_BASE"
echo ""

# 备份 facts 数据
echo "📦 备份 Facts 数据..."
for agent_dir in "$FACTS_BASE"/*/; do
    agent_name=$(basename "$agent_dir")
    
    # 跳过特殊目录
    if [[ "$agent_name" == "."* ]] || [[ "$agent_name" == "shared" ]] || [[ "$agent_name" == "backup" ]]; then
        continue
    fi
    
    facts_dir="$agent_dir/facts"
    if [ -d "$facts_dir" ]; then
        # 备份到带时间戳的目录
        backup_dir="$BACKUP_BASE/facts/${agent_name}_${DATE}"
        cp -r "$facts_dir" "$backup_dir" 2>/dev/null || true
        echo "   ✅ $agent_name → ${agent_name}_${DATE}"
    fi
done
echo ""

# 备份认知画像
echo "📦 备份认知画像..."
for agent_dir in "$FACTS_BASE"/*/; do
    agent_name=$(basename "$agent_dir")
    
    # 跳过特殊目录
    if [[ "$agent_name" == "."* ]] || [[ "$agent_name" == "shared" ]] || [[ "$agent_name" == "backup" ]]; then
        continue
    fi
    
    profile_file="$agent_dir/cognitive_profile.json"
    if [ -f "$profile_file" ]; then
        cp "$profile_file" "$BACKUP_BASE/profiles/${agent_name}_${DATE}.json" 2>/dev/null || true
        echo "   ✅ $agent_name → ${agent_name}_${DATE}.json"
    fi
done
echo ""

# 创建保护标记文件
echo "🛡️ 创建保护标记..."
for agent_dir in "$FACTS_BASE"/*/; do
    agent_name=$(basename "$agent_dir")
    
    # 跳过特殊目录
    if [[ "$agent_name" == "."* ]] || [[ "$agent_name" == "shared" ]] || [[ "$agent_name" == "backup" ]]; then
        continue
    fi
    
    # 创建 DO_NOT_DELETE 标记
    echo "# ⚠️ 重要数据目录" > "$agent_dir/DO_NOT_DELETE.txt"
    echo "" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "此目录包含 Memora v4.0 的重要数据：" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "- facts/ - 认知事实数据" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "- cognitive_profile.json - 认知画像" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "- exp_history.jsonl - EXP 历史记录" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "⚠️ 删除前请确认：" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "1. 已备份数据" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "2. 已获得枢衡授权" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "3. 确认真的需要删除" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "备份位置：$BACKUP_BASE" >> "$agent_dir/DO_NOT_DELETE.txt"
    echo "最后备份：$DATE" >> "$agent_dir/DO_NOT_DELETE.txt"
    
    echo "   ✅ $agent_name/DO_NOT_DELETE.txt"
done
echo ""

# 统计
echo "📊 备份统计"
facts_backup_count=$(ls -d "$BACKUP_BASE/facts"/* 2>/dev/null | wc -l)
profile_backup_count=$(ls "$BACKUP_BASE/profiles"/*.json 2>/dev/null | wc -l)
echo "   Facts 备份：$facts_backup_count 个"
echo "   画像备份：$profile_backup_count 个"
echo ""

echo "=========================================="
echo "  ✅ 数据保护完成！"
echo "=========================================="
echo ""
echo "📚 备份位置：$BACKUP_BASE"
echo "🛡️ 保护标记：已创建到各 Agent 目录"
echo ""
echo "⚠️ 重要提示："
echo ""
echo "   1. 删除任何数据前请先查看 DO_NOT_DELETE.txt"
echo "   2. 定期运行此脚本备份数据"
echo "   3. 建议添加到 cron 定期备份"
echo ""
