# Changelog

All notable changes to this project will be documented in this file.

## [v5.0.6] - 2026-03-22

### Fixed
- ✅ 修复五维认知画像维度分配 Bug
  - creation/metacognition/collaboration 维度始终为 0
  - 根因：所有记忆写入都归到 understanding 维度
- ✅ semantic 记忆正确归到 creation 维度
- ✅ 每日任务按类型分配维度（写日志→metacognition，分享→collaboration 等）

## [v5.0.5] - 2026-03-22

### Fixed
- ✅ 修复 Doctor 硬编码 workspace 路径（workspace-shuheng）
- ✅ 添加自动 workspace 检测逻辑
- ✅ 集成 OpenClaw 身份检测（SOUL.md/IDENTITY.md）
- ✅ SKILL_DIR 改为 anima-aios

## [v5.0.4] - 2026-03-22

### Added
- ✅ 集成 OpenClaw 身份体系（零配置）
- ✅ SOUL.md/IDENTITY.md 自动解析 Agent 名称
- ✅ Doctor 记忆同步工具（--check-sync, --sync-memory）
- ✅ 工作空间名称映射表
- ✅ 7 层身份检测降级机制

## [v5.0.3] - 2026-03-22

### Fixed
- ✅ 修复 3 层同步机制 Bug（记忆只写第 1 层）
- ✅ 修复 EXP 计算错误（C 级质量得 0 EXP）
- ✅ 质量系数只奖励不惩罚
- ✅ Doctor Agent 名称检测修复

## [v5.0.2] - 2026-03-21

### Added
- ✅ 三层记忆同步机制
  - 第一层：实时同步（anima_tools.py）
  - 第二层：启动同步（memory_sync.py）
  - 第三层：定时同步（sync-memory.sh）
- ✅ Doctor 增加记忆同步检查
- ✅ 完整文档（MEMORY_SYNC_GUIDE.md, CODE_REVIEW_20260321.md）

### Changed
- ✅ 优化 anima_tools.py 代码结构
- ✅ 改进错误处理机制

### Fixed
- ✅ 修复两套记忆系统不同步问题
- ✅ 修复 Doctor 检查不完整问题

## [v5.0.1] - 2026-03-21

### Added
- ✅ Anima doctor 自检自修工具
- ✅ 6 项检查（skill/core/配置/数据/依赖/权限）
- ✅ 自动修复功能

## [v5.0.0] - 2026-03-21

### Added
- ✅ 品牌升级：Memora → Anima-AIOS
- ✅ 游戏化成长系统
- ✅ 9 个核心工具
- ✅ 每日任务系统
- ✅ 团队排行榜
