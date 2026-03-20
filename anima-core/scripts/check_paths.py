#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anima-AIOS - 路径兼容性检查

检查所有路径是否可访问，并提供修复建议。

用法：
    python3 scripts/check_paths.py
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.path_config import get_config


def check_path(path: Path, name: str, should_exist: bool = False) -> bool:
    """
    检查路径
    
    Args:
        path: 路径对象
        name: 路径名称
        should_exist: 是否应该存在
    
    Returns:
        检查是否通过
    """
    exists = path.exists()
    
    if should_exist and not exists:
        print(f"❌ {name}: {path} (不存在)")
        return False
    elif not should_exist and not exists:
        print(f"✅ {name}: {path} (路径可创建)")
        return True
    elif exists:
        print(f"✅ {name}: {path} (存在)")
        return True
    else:
        print(f"⚠️  {name}: {path} (状态未知)")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("  Anima-AIOS - 路径兼容性检查")
    print("=" * 60)
    print()
    
    config = get_config()
    
    # 系统信息
    print("📊 系统信息:")
    print(f"  操作系统：{config.system}")
    print(f"  是 Linux: {config.is_linux}")
    print(f"  是 macOS: {config.is_macos}")
    print(f"  是 Windows: {config.is_windows}")
    print()
    
    # 路径检查
    print("📁 路径检查:")
    print()
    
    checks = [
        (config.facts_base, "facts_base", False),
        (config.openclaw_base, "openclaw_base", False),
        (config.agents_dir, "agents_dir", False),
        (config.backup_dir, "backup_dir", False),
        (config.shared_dir, "shared_dir", False),
        (config.message_queue_base, "message_queue_base", False),
        (config.openclaw_agents_dir, "openclaw_agents_dir", False),
    ]
    
    passed = 0
    total = len(checks)
    
    for path, name, should_exist in checks:
        if check_path(path, name, should_exist):
            passed += 1
    
    print()
    print("=" * 60)
    print(f"  检查结果：{passed}/{total} 通过")
    print("=" * 60)
    print()
    
    # 配置导出
    print("⚙️  完整配置:")
    print()
    for key, value in config.to_dict().items():
        print(f"  {key}: {value}")
    print()
    
    # 修复建议
    if passed < total:
        print("💡 修复建议:")
        print()
        
        if not config.facts_base.exists():
            print(f"1. 创建 facts_base 目录:")
            print(f"   mkdir -p {config.facts_base}")
            print()
        
        if not config.openclaw_base.exists():
            print(f"2. 检查 OpenClaw 安装:")
            print(f"   路径：{config.openclaw_base}")
            print()
        
        if not config.openclaw_agents_dir.exists():
            print(f"3. 检查 OpenClaw Agents 目录:")
            print(f"   路径：{config.openclaw_agents_dir}")
            print()
    
    # 返回状态码
    return 0 if passed == total else 1


if __name__ == '__main__':
    sys.exit(main())
