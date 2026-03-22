#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anima-AIOS - 记忆同步模块

第二层：启动同步（兜底机制）
- Anima 启动时检查并补全缺失的记忆
- 从 Workspace 同步到画像目录
"""

import os
import shutil
from pathlib import Path
from datetime import datetime


class MemorySync:
    """记忆同步器"""
    
    def __init__(self, agent_name: str):
        """
        初始化同步器
        
        Args:
            agent_name: Agent 名称
        """
        self.agent_name = agent_name
        self.workspace_mem = Path(os.path.expanduser("~/.openclaw/workspace-shuheng/memory"))
        self.portrait_mem = Path(f"/home/画像/{agent_name}/memory")
        
        # 确保画像目录存在
        self.portrait_mem.mkdir(parents=True, exist_ok=True)
    
    def sync_on_startup(self):
        """
        启动时同步记忆
        
        Returns:
            dict: 同步统计
        """
        stats = {
            'synced': 0,
            'skipped': 0,
            'errors': 0
        }
        
        if not self.workspace_mem.exists():
            print(f"⚠️  Workspace 记忆目录不存在：{self.workspace_mem}")
            return stats
        
        # 同步所有记忆文件
        for mem_file in self.workspace_mem.glob("*.md"):
            if mem_file.name.startswith('.'):
                continue
            
            try:
                dest = self.portrait_mem / mem_file.name
                
                # 如果画像目录没有该文件，则复制
                if not dest.exists():
                    shutil.copy2(mem_file, dest)
                    print(f"✅ 同步记忆：{mem_file.name}")
                    stats['synced'] += 1
                else:
                    # 文件已存在，跳过
                    stats['skipped'] += 1
            except Exception as e:
                print(f"❌ 同步失败 {mem_file.name}: {e}")
                stats['errors'] += 1
        
        return stats
    
    def sync_today(self):
        """
        同步今日记忆
        
        Returns:
            bool: 是否成功
        """
        today = datetime.now().strftime("%Y-%m-%d")
        workspace_today = self.workspace_mem / f"{today}.md"
        portrait_today = self.portrait_mem / f"{today}.md"
        
        if not workspace_today.exists():
            print(f"⚠️  今日记忆不存在：{workspace_today}")
            return False
        
        try:
            # 复制今日记忆
            shutil.copy2(workspace_today, portrait_today)
            print(f"✅ 今日记忆已同步：{today}.md")
            return True
        except Exception as e:
            print(f"❌ 同步今日记忆失败：{e}")
            return False
    
    def check_sync_status(self):
        """
        检查同步状态
        
        Returns:
            dict: 同步状态
        """
        status = {
            'workspace_exists': self.workspace_mem.exists(),
            'portrait_exists': self.portrait_mem.exists(),
            'workspace_files': 0,
            'portrait_files': 0,
            'missing_files': []
        }
        
        if self.workspace_mem.exists():
            status['workspace_files'] = len(list(self.workspace_mem.glob("*.md")))
        
        if self.portrait_mem.exists():
            status['portrait_files'] = len(list(self.portrait_mem.glob("*.md")))
            
            # 检查缺失的文件
            for mem_file in self.workspace_mem.glob("*.md"):
                if mem_file.name.startswith('.'):
                    continue
                
                dest = self.portrait_mem / mem_file.name
                if not dest.exists():
                    status['missing_files'].append(mem_file.name)
        
        return status


def sync_memory_on_startup(agent_name: str):
    """
    Anima 启动时同步记忆
    
    Args:
        agent_name: Agent 名称
    """
    print("=" * 60)
    print("  🔄 同步记忆（启动时）")
    print("=" * 60)
    
    sync = MemorySync(agent_name)
    stats = sync.sync_on_startup()
    
    print()
    print(f"同步完成:")
    print(f"  - 已同步：{stats['synced']} 个文件")
    print(f"  - 已跳过：{stats['skipped']} 个文件")
    print(f"  - 错误：{stats['errors']} 个")
    print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        agent_name = sys.argv[1]
    else:
        agent_name = "枢衡"
    
    sync_memory_on_startup(agent_name)
