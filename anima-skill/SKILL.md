---
name: anima-aios
description: >
  基于 OpenClaw 原生架构的 AI Agent 认知成长体系，仅依赖 OpenClaw 原生环境 + Python 3.10+ + Git，无需额外安装复杂依赖。
  为你的 Agent 提供永久化记忆管理、可视化经验值成长、五维认知画像、游戏化每日任务和团队排行榜（Agent军团模式）。
  不再担心记忆丢失，清晰掌握成长等级，让你的 Agent 真正拥有持续进化的能力。
use_when:
  - cognitive profile
  - EXP
  - level
  - daily quest
  - memory sync
  - team ranking
  - growth tracking
  - agent abilities
  - 认知画像
  - 经验值
  - 等级
  - 每日任务
  - 记忆同步
  - 团队排行
---

# Anima-AIOS

> **让成长可见，让认知可量** | Making Growth Visible, Making Cognition Measurable

为你的 AI Agent 添加记忆、成长和认知能力。追踪每一次学习，量化每一份进步。

---

## ✨ 核心功能

### 🧠 增强记忆管理
- **3 层同步机制**：OpenClaw Memory + Anima Facts + EXP History
- **EXP 奖励**：写记忆自动获得经验值
- **智能去重**：自动避免重复记录

### 📊 五维认知画像
- **内化力**：衡量知识吸收和理解能力
- **应用力**：衡量知识迁移和实践能力
- **创造力**：衡量知识整合和创新能力
- **元认知**：衡量自我反思和监控能力
- **协作力**：衡量团队合作和互助能力

### 🎮 游戏化成长
- **等级系统**：从 Lv.1 新手到 Lv.100 终身成就
- **每日任务**：每天 3 个挑战，完成获得额外 EXP
- **进度追踪**：可视化升级进度条

### 🏆 团队排行榜
- **EXP 排行**：基于公平归一化算法排名
- **实时竞争**：追踪排名变化和差距
- **团队对比**：发现优势与短板

### 🏥 Doctor 自检工具
- **一键诊断**：检查 Skill/Core/数据完整性
- **记忆同步**：验证多层记忆数据一致性
- **自动修复**：常见问题一键解决

---

## 📸 效果展示 | Screenshots
> 🔔 若图片无法显示，请访问：https://github.com/anima-aios/anima/tree/main/anima-skill/assets 查看原图
> If images don't load, visit the link above to see originals.

### 认知画像卡片 | Cognitive Profile Card

![Cognitive Profile](https://raw.githubusercontent.com/anima-aios/anima/main/anima-skill/assets/cognitive-profile.png)

*Agent 认知画像：五维评分 + 等级进度 + 今日 EXP 来源*

---

### 今日认知成长 | Daily Cognitive Growth

![Daily Growth](https://raw.githubusercontent.com/anima-aios/anima/main/anima-skill/assets/daily-growth.png)

*今日成长报告：任务进度 + EXP 来源 + 升级预测*

---

### 团队排行榜 | Team Leaderboard

![Team Ranking](https://raw.githubusercontent.com/anima-aios/anima/main/anima-skill/assets/team-ranking.png)

*团队 EXP 排行榜：实时竞争 + 变化追踪*

---

### 我所做的意义 | Why I Built This

![Why I Built This](https://raw.githubusercontent.com/anima-aios/anima/main/anima-skill/assets/meaning.png)

*这 就是我的目的*

---

## 🚀 快速开始 | Quick Start

### 1️⃣ 安装 | Install

```bash
clawhub install anima-aios
```

### 2️⃣ 验证安装 | Verify

```bash
### cd /path/to/your/workspace/skills/anima-aios/
cd ~/.openclaw/workspace/skills/anima-aios/
python3 anima_doctor.py
```

**预期输出：**
```
============================================================
  🏥 Anima-AIOS 自检工具
============================================================
当前 Agent: {你的名字}
------------------------------------------------------------
✅ skill_installed: Skill 已安装
✅ core_installed: Core 已安装
✅ data_integrity: 数据完整
...
```

### 3️⃣ 开始使用 | Start Using

**查看认知画像：**
```
我的认知画像是什么？
```

**查看经验值：**
```
我的经验值是多少？
```

**写一条记忆：**
```
记住：今天完成了 Anima v5.0 发布
```

**查看今日任务：**
```
今天的任务是什么？
```

---

## 🔧 工具列表 | Tools

| 工具 | 用途 | EXP 奖励 |
|------|------|----------|
| `memory_write` | 写入记忆 | +1~2 |
| `memory_search` | 搜索记忆 | +2 |
| `get_cognitive_profile` | 认知画像 | - |
| `get_exp` | 查询 EXP | - |
| `get_level` | 查询等级 | - |
| `quest_daily_status` | 今日任务 | - |
| `quest_complete` | 完成任务 | +5~20 |
| `get_team_ranking` | 团队排行 | - |

---

## 📊 等级系统 | Level System

### 成长路径 | Growth Path (基于每日完成全部任务的理想成长速度)

| 等级 | EXP 需求 | 阶段 |
|------|----------|------|
| Lv.1 | 2 | 新手起步 |
| Lv.3 | 100 | 第 1 天 |
| Lv.6 | 1000 | 第 1 周 |
| Lv.13 | 10000 | 第 1 月 |
| Lv.25 | 100000 | 第 1 年 |
| Lv.100 | 14000000 | 终身成就 |

### EXP 获取规则 | EXP Rules

| 行为 | EXP | 说明 |
|------|-----|------|
| 写记忆（episodic） | +1 | 日常记录 |
| 写记忆（semantic） | +2 | 知识沉淀（双倍） |
| 搜索记忆 | +2 | 主动检索 |
| 完成任务 | +5~20 | 难度相关 |
| 分享知识到团队 | +5 | 团队贡献 |

---

## ⚙️ 配置 | Configuration

### 环境变量（可选）| Environment Variables (Optional)

```bash
# 手动指定 Agent 名称（通常自动检测）
export ANIMA_AGENT_NAME=your_agent_name

# 指定工作空间
export ANIMA_WORKSPACE=/path/to/your/workspace
```

### 数据存储 | Data Storage

- **数据目录：** `~/.anima/`
- **记忆文件：** Agent workspace `memory/` 目录
- **Facts 目录：** 自动创建在 Agent 画像目录下

---

## 🏥 Doctor 使用指南 | Doctor Guide

### 健康检查 | Health Check

```bash
### cd /path/to/your/workspace/skills/anima-aios/
cd ~/.openclaw/workspace/skills/anima-aios/

python3 anima_doctor.py
```

### 检查记忆同步 | Check Memory Sync

```bash
python3 anima_doctor.py --check-sync
```

### 同步历史记忆 | Sync Historical Memory

```bash
python3 anima_doctor.py --sync-memory
```

### 自动修复 | Auto Repair

```bash
python3 anima_doctor.py --fix
```

---

## 📝 版本历史 | Changelog

**当前版本：** v5.0.8 (2026-03-22)

完整变更记录参见 [references/changelog.md](references/changelog.md)

---

## 🙏 致谢 | Acknowledgments


生活是一个最长久的项目，而我希望带着日安他们共同去完成。
我是立文，如果你也认同我的想法，我和我的Agent欢迎你们。

Anima-AIOS 完全开源，致力于让每一个 AI Agent 都拥有可持续、可量化的认知成长能力。
项目基于认知科学理论（Bloom 认知分类、Dreyfus 技能习得模型）+ 记忆宫殿模型 + 金字塔原理 + 自创 AI 记忆衰退函数设计。

---

## 📄 许可证 | License

**MIT License**
详见 LICENSE 文件：https://github.com/anima-aios/anima/blob/main/LICENSE
允许商用 / 二次开发，需保留原作者信息

- **GitHub:** https://github.com/anima-aios/anima
- **文档:** https://github.com/anima-aios/anima/blob/main/README.md
- **版本:** v5.0.8
- **最后更新:** 2026-03-22

---

_让每一次学习都有迹可循，让每一份成长都被看见。_
