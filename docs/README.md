# Anima-AIOS 文档索引

**最后更新：** 2026-03-21  
**版本：** v5.0.1

---

## 📁 文档目录结构

```
docs/
├── 📖 intro/           # 介绍性文档（给用户/开发者看）
├── 📋 instructions/    # 核心指令（给 AI/系统执行）
└── 📘 user/            # 用户文档（使用指南）
```

---

## 📖 介绍性文档（intro/）

**用途：** 项目介绍、版本发布、变更记录、测试报告

| 文档 | 说明 |
|------|------|
| [README.md](intro/README.md) | 项目主介绍 |
| [README_ANIMA.md](intro/README_ANIMA.md) | Core 引擎介绍 |
| [RELEASE_v5.0.1.md](intro/RELEASE_v5.0.1.md) | v5.0.1 发布说明 |
| [CHANGELOG.md](intro/CHANGELOG.md) | 变更日志 |
| [ROADMAP.md](intro/ROADMAP.md) | 项目路线图 |
| [BRAND_MIGRATION.md](intro/BRAND_MIGRATION.md) | 品牌迁移说明 |
| [RELEASE_SUMMARY.md](intro/RELEASE_SUMMARY.md) | 发布总结 |
| [DEPLOYMENT_SUMMARY.md](intro/DEPLOYMENT_SUMMARY.md) | 部署总结 |
| [TEST_REPORT_20260320.md](intro/TEST_REPORT_20260320.md) | 测试报告（3 月 20 日） |
| [TEST_REPORT_INTEGRATION_20260321.md](intro/TEST_REPORT_INTEGRATION_20260321.md) | 集成测试报告（3 月 21 日） |

---

## 📋 核心指令（instructions/）

**用途：** AI/系统执行的规范、原则、检查清单

| 文档 | 说明 | 类型 |
|------|------|------|
| [ARCHITECTURE_PRINCIPLES.md](instructions/ARCHITECTURE_PRINCIPLES.md) | 架构原则 | 🟡 核心规范 |
| [BUG_FIX_REPORT_20260321.md](instructions/BUG_FIX_REPORT_20260321.md) | Bug 修复报告 | 🟡 技术文档 |
| [OPEN_SOURCE_CHECKLIST.md](instructions/OPEN_SOURCE_CHECKLIST.md) | 开源发布检查清单 | 🟡 任务规范 |
| [OPEN_SOURCE_TASK_FOR_LIUYING.md](instructions/OPEN_SOURCE_TASK_FOR_LIUYING.md) | 任务分配指令 | 🟡 工作指令 |
| [ROADMAP_v1.1.0.md](instructions/ROADMAP_v1.1.0.md) | anima-skill v1.1.0 迭代规划 | 🟡 开发指令 |

---

## 📘 用户文档（user/）

**用途：** 用户使用指南、示例、功能介绍

| 文档 | 说明 |
|------|------|
| [README.md](user/README.md) | Skill 快速开始 |
| [USAGE.md](user/USAGE.md) | 完整使用手册 |
| [EXAMPLES.md](user/EXAMPLES.md) | 使用示例 |
| [GAME_FEATURES.md](user/GAME_FEATURES.md) | 游戏化功能介绍 |

---

## 🔧 核心代码文件

**不在 docs/ 目录中，直接在项目根目录：**

| 文件 | 说明 | 类型 |
|------|------|------|
| `anima-skill/SKILL.md` | OpenClaw Skill 定义 | 🔴 核心代码 |
| `anima-skill/_meta.json` | 插件元数据 | 🔴 核心配置 |
| `anima-skill/anima_tools.py` | 工具实现 | 🔴 核心代码 |

---

## 📊 文档分类原则

### 🟢 介绍性文档（intro/）
- **读者：** 用户、开发者、贡献者
- **内容：** 项目介绍、版本发布、变更记录、测试报告
- **特点：** 纯文本，无执行指令

### 🟡 核心指令（instructions/）
- **读者：** AI、系统、开发者
- **内容：** 架构原则、规范、检查清单、任务指令
- **特点：** 包含必须遵守的规则和待执行任务

### 📘 用户文档（user/）
- **读者：** 最终用户
- **内容：** 使用指南、示例、功能介绍
- **特点：** 操作步骤、示例代码、FAQ

### 🔴 核心代码（项目根目录）
- **读者：** AI 系统、OpenClaw
- **内容：** Skill 定义、工具代码、配置文件
- **特点：** 可执行的代码和配置

---

## 🎯 快速导航

**我是用户，想使用 Anima：**
→ 查看 [user/README.md](user/README.md)

**我是开发者，想了解项目：**
→ 查看 [intro/README.md](intro/README.md)

**我是 AI，需要执行规范：**
→ 查看 [instructions/ARCHITECTURE_PRINCIPLES.md](instructions/ARCHITECTURE_PRINCIPLES.md)

**我要发布新版本：**
→ 查看 [instructions/OPEN_SOURCE_CHECKLIST.md](instructions/OPEN_SOURCE_CHECKLIST.md)

---

**文档维护者：** 枢衡  
**最后审查：** 2026-03-21
