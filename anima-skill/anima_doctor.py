#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anima Doctor - Anima-AIOS 自检自修工具

用法:
    anima doctor              # 自检
    anima doctor --fix        # 自修
    anima doctor --fix --yes  # 自动修复（无需确认）
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

# 项目路径
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace-shuheng"))
ANIMA_HOME = Path(os.path.expanduser("~/.anima"))
SKILL_DIR = WORKSPACE / "projects" / "anima" / "anima-skill"
CORE_DIR = WORKSPACE / "projects" / "anima" / "anima-core"


class AnimaDoctor:
    """Anima 自检自修工具"""
    
    def __init__(self):
        """初始化医生"""
        self.checks = {}
        self.fixes = []
    
    def diagnose(self, auto_fix=False, auto_confirm=False):
        """
        自检 Anima 状态
        
        Args:
            auto_fix: 是否自动修复
            auto_confirm: 是否自动确认修复
        """
        print("=" * 60)
        print("  🏥 Anima-AIOS 自检工具")
        print("=" * 60)
        print(f"  时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        print()
        
        # 执行检查
        self._check_skill_installed()
        self._check_core_installed()
        self._check_config()
        self._check_data_integrity()
        self._check_dependencies()
        self._check_permissions()
        
        # 打印结果
        self._print_results()
        
        # 发现问题时提示修复
        has_issues = any(check['status'] != 'ok' for check in self.checks.values())
        
        if has_issues:
            print("\n⚠️  检测到问题，建议修复")
            
            if auto_fix:
                if auto_confirm or self._user_confirm("执行修复？"):
                    self.recover()
            else:
                print("\n💡 提示：运行以下命令修复")
                print("   anima doctor --fix")
        
        return has_issues
    
    def _check_skill_installed(self):
        """检查 skill 是否安装"""
        skill_files = [
            SKILL_DIR / "SKILL.md",
            SKILL_DIR / "_meta.json",
            SKILL_DIR / "anima_tools.py",
        ]
        
        missing = [f for f in skill_files if not f.exists()]
        
        if missing:
            self.checks['skill_installed'] = {
                'status': 'error',
                'message': f'Skill 未安装，缺失文件：{len(missing)} 个',
                'fix': '运行 clawhub install anima 或手动安装'
            }
        else:
            self.checks['skill_installed'] = {
                'status': 'ok',
                'message': 'Skill 已安装'
            }
    
    def _check_core_installed(self):
        """检查 core 是否安装"""
        core_files = [
            ANIMA_HOME / "core" / "exp_tracker.py",
            ANIMA_HOME / "core" / "cognitive_profile.py",
            ANIMA_HOME / "core" / "dimension_calculator.py",
        ]
        
        missing = [f for f in core_files if not f.exists()]
        
        if missing:
            self.checks['core_installed'] = {
                'status': 'warning',
                'message': f'Core 未完全安装，缺失文件：{len(missing)} 个',
                'fix': '运行 post-install.sh 或重新安装'
            }
        else:
            self.checks['core_installed'] = {
                'status': 'ok',
                'message': 'Core 已安装'
            }
    
    def _check_config(self):
        """检查配置文件"""
        config_file = ANIMA_HOME / "anima_config.json"
        
        if not config_file.exists():
            self.checks['config'] = {
                'status': 'warning',
                'message': '配置文件不存在',
                'fix': '创建默认配置文件'
            }
        else:
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    config = json.load(f)
                
                # 检查必要配置
                required_keys = ['exp', 'quest', 'profile']
                missing_keys = [k for k in required_keys if k not in config]
                
                if missing_keys:
                    self.checks['config'] = {
                        'status': 'warning',
                        'message': f'配置不完整，缺失：{missing_keys}',
                        'fix': '补充配置项'
                    }
                else:
                    self.checks['config'] = {
                        'status': 'ok',
                        'message': '配置正确'
                    }
            except json.JSONDecodeError:
                self.checks['config'] = {
                    'status': 'error',
                    'message': '配置文件格式错误',
                    'fix': '修复或重建配置文件'
                }
    
    def _check_data_integrity(self):
        """检查数据完整性"""
        # 检查 EXP 历史
        exp_file = ANIMA_HOME / "exp_history.jsonl"
        if exp_file.exists():
            try:
                with open(exp_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                self.checks['data_integrity'] = {
                    'status': 'ok',
                    'message': f'数据完整 ({len(lines)} 条记录)'
                }
            except Exception as e:
                self.checks['data_integrity'] = {
                    'status': 'error',
                    'message': f'数据文件损坏：{e}',
                    'fix': '从备份恢复数据'
                }
        else:
            self.checks['data_integrity'] = {
                'status': 'warning',
                'message': 'EXP 历史文件不存在（首次使用正常）',
                'fix': '开始使用后自动生成'
            }
    
    def _check_dependencies(self):
        """检查依赖"""
        missing_deps = []
        
        # 检查 Python 包
        try:
            import inotify
        except ImportError:
            missing_deps.append('inotify')
        
        try:
            import requests
        except ImportError:
            missing_deps.append('requests')
        
        if missing_deps:
            self.checks['dependencies'] = {
                'status': 'error',
                'message': f'缺少依赖：{", ".join(missing_deps)}',
                'fix': f'pip install {" ".join(missing_deps)}'
            }
        else:
            self.checks['dependencies'] = {
                'status': 'ok',
                'message': '依赖齐全'
            }
    
    def _check_permissions(self):
        """检查权限"""
        # 检查关键目录权限
        dirs_to_check = [
            ANIMA_HOME,
            WORKSPACE / "memory",
        ]
        
        permission_issues = []
        for dir_path in dirs_to_check:
            if dir_path.exists():
                if not os.access(dir_path, os.W_OK):
                    permission_issues.append(str(dir_path))
        
        if permission_issues:
            self.checks['permissions'] = {
                'status': 'error',
                'message': f'无写入权限：{len(permission_issues)} 个目录',
                'fix': 'chmod -R 755 ' + ' '.join(permission_issues)
            }
        else:
            self.checks['permissions'] = {
                'status': 'ok',
                'message': '权限正常'
            }
    
    def _print_results(self):
        """打印检查结果"""
        print("诊断结果:")
        print("-" * 60)
        
        for check_name, check_result in self.checks.items():
            status_icon = {
                'ok': '✅',
                'warning': '⚠️',
                'error': '❌'
            }.get(check_result['status'], '❓')
            
            print(f"{status_icon} {check_name}: {check_result['message']}")
        
        print("-" * 60)
        
        ok_count = sum(1 for c in self.checks.values() if c['status'] == 'ok')
        warning_count = sum(1 for c in self.checks.values() if c['status'] == 'warning')
        error_count = sum(1 for c in self.checks.values() if c['status'] == 'error')
        
        print(f"总计：{ok_count} 正常，{warning_count} 警告，{error_count} 错误")
    
    def _user_confirm(self, message):
        """用户确认"""
        response = input(f"{message} (y/N): ")
        return response.lower() in ['y', 'yes']
    
    def recover(self):
        """自修 Anima 问题"""
        print("\n开始自动修复...")
        print("-" * 60)
        
        fixes = []
        
        # 1. 修复配置文件
        if self.checks.get('config', {}).get('status') != 'ok':
            if self._fix_config():
                fixes.append('config_fixed')
        
        # 2. 修复依赖
        if self.checks.get('dependencies', {}).get('status') != 'ok':
            if self._fix_dependencies():
                fixes.append('dependencies_fixed')
        
        # 3. 修复权限
        if self.checks.get('permissions', {}).get('status') != 'ok':
            if self._fix_permissions():
                fixes.append('permissions_fixed')
        
        # 4. 重新安装 core
        if self.checks.get('core_installed', {}).get('status') == 'error':
            if self._reinstall_core():
                fixes.append('core_reinstalled')
        
        # 打印修复结果
        print("-" * 60)
        if fixes:
            print("修复结果:")
            for fix in fixes:
                print(f"✅ {fix}")
            print("-" * 60)
            print("✅ 修复完成！建议重新运行 anima doctor 验证")
        else:
            print("⚠️  部分问题需要手动修复，请查看上方提示")
        
        return fixes
    
    def _fix_config(self):
        """修复配置文件"""
        try:
            config_file = ANIMA_HOME / "anima_config.json"
            config_file.parent.mkdir(parents=True, exist_ok=True)
            
            default_config = {
                "exp": {
                    "enabled": True,
                    "dailyLimit": 100
                },
                "quest": {
                    "enabled": True,
                    "autoRefresh": True
                },
                "profile": {
                    "autoUpdate": True,
                    "updateInterval": 3600
                },
                "data": {
                    "backupEnabled": True,
                    "backupTime": "03:00"
                }
            }
            
            with open(config_file, "w", encoding="utf-8") as f:
                json.dump(default_config, f, ensure_ascii=False, indent=2)
            
            print("✅ 配置文件已创建")
            return True
        except Exception as e:
            print(f"❌ 创建配置文件失败：{e}")
            return False
    
    def _fix_dependencies(self):
        """修复依赖"""
        try:
            print("正在安装依赖...")
            subprocess.run([sys.executable, "-m", "pip", "install", "inotify", "requests"], check=True)
            print("✅ 依赖已安装")
            return True
        except Exception as e:
            print(f"❌ 安装依赖失败：{e}")
            print("💡 请手动运行：pip install inotify requests")
            return False
    
    def _fix_permissions(self):
        """修复权限"""
        try:
            dirs_to_fix = [
                ANIMA_HOME,
                WORKSPACE / "memory",
            ]
            
            for dir_path in dirs_to_fix:
                if dir_path.exists():
                    subprocess.run(["chmod", "-R", "755", str(dir_path)], check=True)
            
            print("✅ 权限已修复")
            return True
        except Exception as e:
            print(f"❌ 修复权限失败：{e}")
            return False
    
    def _reinstall_core(self):
        """重新安装 core"""
        try:
            print("正在重新安装 core...")
            
            # 运行 post-install.sh
            post_install = SKILL_DIR / "post-install.sh"
            if post_install.exists():
                subprocess.run(["bash", str(post_install)], check=True)
                print("✅ core 已重新安装")
                return True
            else:
                print("❌ 找不到 post-install.sh")
                return False
        except Exception as e:
            print(f"❌ 重新安装 core 失败：{e}")
            return False


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Anima-AIOS 自检自修工具')
    parser.add_argument('--fix', action='store_true', help='自检并修复')
    parser.add_argument('--yes', '-y', action='store_true', help='自动确认修复')
    parser.add_argument('--auto', '-a', action='store_true', help='自动模式（无需确认）')
    
    args = parser.parse_args()
    
    doctor = AnimaDoctor()
    
    if args.fix:
        doctor.diagnose(auto_fix=True, auto_confirm=args.auto or args.yes)
    else:
        doctor.diagnose()


if __name__ == "__main__":
    main()
