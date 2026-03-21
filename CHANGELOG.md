# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Planned
- v5.1.0: 成就徽章系统
- v5.2.0: 周期性挑战

---

## [skill-v5.0.1] - 2026-03-21

### Fixed
- **Bug 001**: 维度名称不一致 - 统一使用 `understanding`
- **Bug 002**: EXP 记录静默失败 - 添加具体异常处理和错误日志
- **Bug 005**: 去重检测未实现 - 基于内容哈希检查最近 10 条记忆
- **Bug 008**: 静默失败过多 - 修复 4 处 bare except
- **Bug 009**: 硬编码 Agent 名称 - 从环境变量 `ANIMA_AGENT_NAME` 获取
- **Bug 010**: 路径配置混乱 - 统一为 `ANIMA_WORKSPACE` 和 `ANIMA_FACTS_BASE`

### Changed
- 质量系数逻辑优化 - 基础 EXP 和质量奖励分开计算

---

## [core-v5.1] - 2026-03-21

### Fixed
- **Bug 003**: 两套等级系统冲突 - 废弃 `normalization_engine.py` 的等级计算
- **Bug 004**: 画像文件不实时更新 - 查询时自动保存
- **Bug 006**: 质量系数逻辑 - 基础 EXP 计入上限，质量奖励作为额外奖励
- **Bug 007**: 权重配置未落地 - creation 维度 EXP 提升 20-25%

### Changed
- `normalization_engine.py:score_to_level()` 标记为已废弃
- `cognitive_profile.py:generate_profile()` 添加 `auto_save` 参数
- `dimension_calculator.py` 按权重调整 EXP 获取规则

### Deprecated
- `normalization_engine.py:score_to_level()` - 请使用 `level_system.py`

---

## [skill-v5.0.0] - 2026-03-21

### Added
- 游戏化成长系统
- 9 个核心工具（memory_search_v2, memory_write_v2, get_cognitive_profile 等）
- 每日任务系统
- 团队排行榜
- 质量评估系统（S/A/B/C 四级）
- 自动安装脚本（post-install.sh）
- 降级模式（core 未安装时仍可用基础功能）

### Changed
- 品牌升级：Memora → Anima-AIOS

---

## [core-v5.0] - 2026-03-21

### Added
- EXP 追踪器（多维度 + 每日限额）
- 认知画像生成器（五维评估）
- 等级系统（累积 EXP 公式）
- 归一化引擎（团队公平比较）
- 每日任务系统（智能生成）
- 数据保护（5 层机制）

### Changed
- 品牌升级：Memora → Anima-AIOS
- 目录统一：anima/, anima-core/, anima-skill/

---

**版本：** v5.0.1 (skill) / v5.1 (core)  
**发布日期：** 2026-03-21  
**GitHub:** https://github.com/anima-aios/anima
