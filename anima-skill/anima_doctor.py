#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anima Doctor v2 - Anima-AIOS 自检自修工具（配置化版本）

用法:
    anima doctor              # 自检当前 Agent
    anima doctor --agent 枢衡  # 自检指定 Agent
    anima doctor --all         # 自检所有 Agent
    anima doctor --fix         # 自修
    anima doctor --fix --yes   # 自动修复（无需确认）

设计原则:
1. 无硬编码 - 所有路径从配置获取
2. 支持多 Agent - 可以诊断任意 Agent
3. 动态计算 - 不依赖静态文件
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

# 工作空间路径
WORKSPACE = Path(os.path.expanduser("~/.openclaw/workspace-shuheng"))
from typing import Dict, List, Optional

# 导入配置模块
CORE_DIR = Path(__file__).parent.parent / 'anima-core' / 'core'
sys.path.insert(0, str(CORE_DIR / 'config'))

try:
    from path_config import get_config
except ImportError:
    # Fallback: 使用默认配置
    class DefaultConfig:
        facts_base = Path('/home/画像')
        anima_core_dir = CORE_DIR
        backup_dir = Path('/home/画像/.backup')
    
    def get_config():
        return DefaultConfig()


class AnimaDoctor:
    """Anima 自检自修工具（配置化版本）"""
    
    def __init__(self, agent_name: Optional[str] = None):
        """
        初始化医生
        
        Args:
            agent_name: Agent 名称（可选，不传则使用当前 Agent）
        """
        self.config = get_config()
        self.agent_name = agent_name or self._get_current_agent()
        self.agent_dir = Path(self.config.facts_base) / self.agent_name
        self.checks = {}
        self.fixes = []
    
    def _get_current_agent(self) -> str:
        """获取当前 Agent 名称"""
        # 优先级：
        # 1. 环境变量 ANIMA_AGENT_NAME
        # 2. OpenClaw 会话上下文（TODO）
        # 3. 默认值 'Agent'
        
        agent_name = os.getenv('ANIMA_AGENT_NAME')
        
        if not agent_name:
            # TODO: 从 OpenClaw 会话上下文获取
            agent_name = 'Agent'
        
        return agent_name
    
    def diagnose(self, auto_fix=False, auto_confirm=False) -> bool:
        """
        自检 Anima 状态
        
        Args:
            auto_fix: 是否自动修复
            auto_confirm: 是否自动确认修复
        
        Returns:
            是否有问题
        """
        print("=" * 60)
        print(f"  🏥 Anima-AIOS 自检工具 - {self.agent_name}")
        print("=" * 60)
        print(f"  时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  路径：{self.config.facts_base}")
        print("=" * 60)
        print()
        
        # 执行检查
        self._check_skill_installed()
        self._check_core_installed()
        self._check_exp_data()
        self._check_profile_dynamic()
        self._check_memory_files()
        self._check_memory_sync()
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
                print(f"   anima doctor --agent {self.agent_name} --fix")
        
        return has_issues
    
    def diagnose_all_agents(self) -> Dict[str, bool]:
        """
        诊断所有 Agent
        
        Returns:
            每个 Agent 的诊断结果
        """
        sys.path.insert(0, str(CORE_DIR))
        from team_scanner import TeamScanner
        
        scanner = TeamScanner()
        agents = scanner.scan_active_agents()
        
        results = {}
        for agent_name in agents:
            doctor = AnimaDoctor(agent_name)
            results[agent_name] = doctor.diagnose()
        
        return results
    
    def _check_skill_installed(self):
        """检查 skill 是否安装"""
        skill_dir = Path(__file__).parent
        skill_files = [
            skill_dir / "SKILL.md",
            skill_dir / "_meta.json",
            skill_dir / "anima_tools.py",
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
            self.config.anima_core_dir / "exp_tracker.py",
            self.config.anima_core_dir / "cognitive_profile.py",
            self.config.anima_core_dir / "level_system.py",
        ]
        
        missing = [f for f in core_files if not f.exists()]
        
        if missing:
            self.checks['core_installed'] = {
                'status': 'error',
                'message': f'Core 未安装，缺失文件：{len(missing)} 个',
                'fix': '运行 anima install-core 或手动安装'
            }
        else:
            self.checks['core_installed'] = {
                'status': 'ok',
                'message': 'Core 已安装'
            }
    
    def _check_exp_data(self):
        """检查 EXP 数据"""
        exp_file = self.agent_dir / 'exp_history.jsonl'
        
        if not exp_file.exists():
            self.checks['exp_data'] = {
                'status': 'warning',
                'message': 'EXP 历史文件不存在',
                'fix': '运行 session_scanner 初始化'
            }
            return
        
        # 计算总 EXP
        total_exp = 0
        with open(exp_file) as f:
            for line in f:
                try:
                    record = json.loads(line)
                    total_exp += record.get('exp', 0)
                except:
                    continue
        
        # 验证等级计算
        expected_level = max(1, int(total_exp ** 0.28))
        
        self.checks['exp_data'] = {
            'status': 'ok',
            'message': f'EXP 总计 {total_exp}，等级 Lv.{expected_level}',
            'details': {'total_exp': total_exp, 'expected_level': expected_level}
        }
    
    def _check_profile_dynamic(self):
        """检查画像是否动态计算"""
        try:
            sys.path.insert(0, str(self.config.anima_core_dir))
            from cognitive_profile import CognitiveProfileGenerator
            from level_system import LevelSystem
            
            generator = CognitiveProfileGenerator(self.agent_name, str(self.config.facts_base))
            profile = generator.generate_profile(auto_scan=False)
            
            level_sys = LevelSystem(self.agent_name, str(self.config.facts_base))
            expected_level = level_sys.get_level_info()['level']
            
            if profile['level'] != expected_level:
                self.checks['profile_dynamic'] = {
                    'status': 'error',
                    'message': f'画像等级 ({profile["level"]}) 与 EXP 等级 ({expected_level}) 不一致',
                    'fix': '更新代码到最新版本'
                }
            else:
                self.checks['profile_dynamic'] = {
                    'status': 'ok',
                    'message': f'画像动态计算正常 (Lv.{profile["level"]})'
                }
        except Exception as e:
            self.checks['profile_dynamic'] = {
                'status': 'error',
                'message': f'画像生成失败：{e}',
                'fix': '检查 core 安装'
            }
    
    def _check_memory_files(self):
        """检查记忆文件"""
        memory_dir = self.agent_dir / 'memory'
        facts_dir = self.agent_dir / 'facts'
        
        today = datetime.now().strftime('%Y-%m-%d')
        today_file = memory_dir / f'{today}.md'
        
        if not self.agent_dir.exists():
            self.checks['memory_files'] = {
                'status': 'error',
                'message': 'Agent 目录不存在',
                'fix': '运行 init 命令初始化'
            }
        elif not memory_dir.exists():
            self.checks['memory_files'] = {
                'status': 'warning',
                'message': '记忆目录不存在',
                'fix': '开始写第一条记忆吧！'
            }
        elif not today_file.exists():
            self.checks['memory_files'] = {
                'status': 'warning',
                'message': f'今日记忆文件不存在 ({today}.md)',
                'fix': '开始写今天的记忆吧！'
            }
        else:
            self.checks['memory_files'] = {
                'status': 'ok',
                'message': '记忆文件正常'
            }
    
    def _check_config(self):
        """检查配置文件"""
        config_file = self.agent_dir / 'anima_config.json'
        
        if not config_file.exists():
            self.checks['config'] = {
                'status': 'warning',
                'message': '配置文件不存在（可选）',
                'fix': '运行 anima init-config 创建默认配置'
            }
        else:
            try:
                with open(config_file) as f:
                    config = json.load(f)
                
                self.checks['config'] = {
                    'status': 'ok',
                    'message': '配置文件正常'
                }
            except Exception as e:
                self.checks['config'] = {
                    'status': 'error',
                    'message': f'配置文件损坏：{e}',
                    'fix': '删除并重新创建配置文件'
                }
    
    def _check_data_integrity(self):
        """检查数据完整性"""
        issues = []
        
        # 检查 facts 目录
        facts_dir = self.agent_dir / 'facts'
        if facts_dir.exists():
            episodic_count = len(list((facts_dir / 'episodic').glob('*.md'))) if (facts_dir / 'episodic').exists() else 0
            semantic_count = len(list((facts_dir / 'semantic').glob('*.md'))) if (facts_dir / 'semantic').exists() else 0
            
            # 修复：使用 rglob 递归查找所有子目录，支持.md 和.json 格式
            episodic_count = len(list((facts_dir / 'episodic').rglob('*.md'))) + len(list((facts_dir / 'episodic').rglob('*.json'))) if (facts_dir / 'episodic').exists() else 0
            semantic_count = len(list((facts_dir / 'semantic').rglob('*.md'))) + len(list((facts_dir / 'semantic').rglob('*.json'))) if (facts_dir / 'semantic').exists() else 0
            
            if episodic_count + semantic_count == 0:
                issues.append(f'facts 目录为空 (episodic: {episodic_count}, semantic: {semantic_count})')
            else:
                # 有数据，正常
                self.checks['data_integrity'] = {
                    'status': 'ok',
                    'message': f'数据完整 (episodic: {episodic_count}, semantic: {semantic_count})'
                }
                return
        
        if issues:
            self.checks['data_integrity'] = {
                'status': 'warning',
                'message': ', '.join(issues),
                'fix': '检查数据是否被误删'
            }
        else:
            self.checks['data_integrity'] = {
                'status': 'ok',
                'message': '数据完整性正常'
            }
    
    def _check_dependencies(self):
        """检查依赖"""
        try:
            import inotify
            import requests
            self.checks['dependencies'] = {
                'status': 'ok',
                'message': '依赖正常'
            }
        except ImportError as e:
            self.checks['dependencies'] = {
                'status': 'error',
                'message': f'缺少依赖：{e.name}',
                'fix': '运行 pip install inotify requests'
            }
    
    def _check_permissions(self):
        """检查权限"""
        dirs_to_check = [
            self.config.facts_base,
            self.agent_dir,
        ]
        
        issues = []
        for dir_path in dirs_to_check:
            if dir_path.exists() and not os.access(dir_path, os.R_OK | os.W_OK):
                issues.append(f'{dir_path} 权限不足')
        
        if issues:
            self.checks['permissions'] = {
                'status': 'error',
                'message': ', '.join(issues),
                'fix': '运行 chmod -R 755 修复权限'
            }
        else:
            self.checks['permissions'] = {
                'status': 'ok',
                'message': '权限正常'
            }
    
    def _check_memory_sync(self):
        """检查记忆同步状态"""
        workspace_mem = WORKSPACE / "memory"
        portrait_mem = Path(f"/home/画像/{self.agent_name}/memory")
        
        # 检查今日记忆
        today = datetime.now().strftime("%Y-%m-%d")
        workspace_today = workspace_mem / f"{today}.md"
        portrait_today = portrait_mem / f"{today}.md"
        
        if workspace_today.exists() and not portrait_today.exists():
            self.checks['memory_sync'] = {
                'status': 'error',
                'message': '记忆未同步到画像目录',
                'fix': '运行 sync-memory.sh 或重新写入记忆'
            }
        elif workspace_today.exists() and portrait_today.exists():
            self.checks['memory_sync'] = {
                'status': 'ok',
                'message': '记忆同步正常'
            }
        else:
            self.checks['memory_sync'] = {
                'status': 'warning',
                'message': '今日无记忆（首次使用正常）',
                'fix': '开始写入记忆后会自动同步'
            }
    
    def _print_results(self):
        """打印检查结果"""
        print("\n诊断结果:")
        print("-" * 60)
        
        ok_count = sum(1 for check in self.checks.values() if check['status'] == 'ok')
        warning_count = sum(1 for check in self.checks.values() if check['status'] == 'warning')
        error_count = sum(1 for check in self.checks.values() if check['status'] == 'error')
        
        for check_name, check_data in self.checks.items():
            status = check_data['status']
            message = check_data['message']
            
            if status == 'ok':
                print(f"✅ {check_name}: {message}")
            elif status == 'warning':
                print(f"⚠️  {check_name}: {message}")
            else:
                print(f"❌ {check_name}: {message}")
        
        print("-" * 60)
        print(f"总计：{ok_count} 正常，{warning_count} 警告，{error_count} 错误")
    
    def _user_confirm(self, message) -> bool:
        """用户确认"""
        response = input(f"{message} (y/N): ")
        return response.lower() == 'y'
    
    def recover(self):
        """修复问题"""
        print("\n执行修复...")
        print("-" * 60)
        
        for check_name, check_data in self.checks.items():
            if check_data['status'] != 'ok':
                fix_method = getattr(self, f'_fix_{check_name}', None)
                if fix_method:
                    print(f"\n修复 {check_name}...")
                    fix_method()
        
        print("-" * 60)
        print("修复完成")
    
    def _fix_config(self):
        """修复配置文件"""
        config_file = self.agent_dir / 'anima_config.json'
        
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
                "autoUpdate": True
            },
            "data": {
                "backupEnabled": True,
                "backupTime": "03:00"
            }
        }
        
        config_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(default_config, f, ensure_ascii=False, indent=2)
        
        print("✅ 配置文件已创建")
        
        # 更新检查状态
        self.checks['config'] = {
            'status': 'ok',
            'message': '配置文件已创建'
        }
    
    def _fix_dependencies(self):
        """修复依赖"""
        try:
            print("正在安装依赖...")
            subprocess.run([sys.executable, "-m", "pip", "install", "inotify", "requests"], check=True)
            print("✅ 依赖已安装")
        except Exception as e:
            print(f"❌ 安装依赖失败：{e}")
            print("💡 请手动运行：pip install inotify requests")
    
    def _fix_permissions(self):
        """修复权限"""
        try:
            dirs_to_fix = [
                self.config.facts_base,
                self.agent_dir,
            ]
            
            for dir_path in dirs_to_fix:
                if dir_path.exists():
                    subprocess.run(["chmod", "-R", "755", str(dir_path)], check=True)
            
            print("✅ 权限已修复")
        except Exception as e:
            print(f"❌ 修复权限失败：{e}")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Anima-AIOS 自检自修工具（配置化版本）')
    parser.add_argument('--agent', '-a', type=str, help='指定 Agent 名称')
    parser.add_argument('--all', action='store_true', help='诊断所有 Agent')
    parser.add_argument('--fix', action='store_true', help='自检并修复')
    parser.add_argument('--yes', '-y', action='store_true', help='自动确认修复')
    parser.add_argument('--auto', action='store_true', help='自动模式（无需确认）')
    
    args = parser.parse_args()
    
    if args.all:
        # 诊断所有 Agent
        doctor = AnimaDoctor()
        results = doctor.diagnose_all_agents()
        
        print("\n" + "=" * 60)
        print("所有 Agent 诊断结果:")
        print("=" * 60)
        for agent_name, has_issues in results.items():
            status = "⚠️  有问题" if has_issues else "✅ 正常"
            print(f"{agent_name}: {status}")
    else:
        # 诊断指定 Agent 或当前 Agent
        doctor = AnimaDoctor(args.agent)
        
        if args.fix:
            doctor.diagnose(auto_fix=True, auto_confirm=args.auto or args.yes)
        else:
            doctor.diagnose()


if __name__ == "__main__":
    main()
