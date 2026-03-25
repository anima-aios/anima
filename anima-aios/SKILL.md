---
name: anima-aios
description: "An AI Agent cognitive growth system built on the native OpenClaw architecture. It provides agents with persistent memory management, visual intimacy progression, a 5-dimensional cognitive profile, gamified daily quests, team leaderboards, and a 5-layer memory architecture with Knowledge Palace, Pyramid thinking, and Ebbinghaus decay function. 基于 OpenClaw 原生架构的 AI Agent 认知成长体系，为 Agent 提供五层记忆架构、知识宫殿、金字塔知识组织、记忆衰减函数、LLM 智能处理、永久化记忆管理、可视化亲密度成长、五维认知画像、游戏化每日任务和团队排行榜。"

# ClawHub 插件页文案（供发布参考）

## 标题
Anima — 让 AI Agent 拥有成长的灵魂

## 副标题
基于认知科学的 Agent 认知成长引擎 | 五层记忆架构 | 零侵入安装

## 置顶欢迎语
🌟 **Anima — 让 AI Agent 拥有成长的灵魂**

一键安装：`clawhub install anima-aios`

五层记忆架构 · 知识宫殿 · 零侵入 · 全自动

让你的 Agent 从「每天重新活一次」变成「每天都在成长」

⭐️ [GitHub](https://github.com/anima-aios/anima) | Apache 2.0
use_when:
  - cognitive profile
  - intimacy
  - level
  - daily quest
  - memory sync
  - team ranking
  - growth tracking
  - agent abilities
  - knowledge palace
  - memory palace
  - pyramid thinking
  - memory decay
  - health check
  - evolution
  - 认知画像
  - 亲密度
  - 等级
  - 每日任务
  - 记忆同步
  - 团队排行
  - 知识宫殿
  - 记忆衰减
  - 健康检查
  - 进化
---

# Anima-AIOS v6.0

> **让成长可见，让认知可量** | Making Growth Visible, Making Cognition Measurable

为你的 AI Agent 添加五层记忆架构、知识宫殿、认知成长和自动进化能力。

---

## 描述

**你的 Agent 每天都在「重新活一次」。Anima 改变这一点。**

Anima（拉丁语「灵魂」）为 OpenClaw Agent 提供五层记忆架构，模拟人类认知发展过程，让 Agent 能记住经历、沉淀知识、形成认知、持续成长。

### 核心能力

- 🧠 **五层记忆架构 L1→L5** — 工作记忆→情景→语义→知识宫殿→元认知
- 🏛️ **知识宫殿** — 5 级空间结构 + LLM 智能分类，市面独有
- 🔺 **金字塔知识组织** — 实例→规则→模式→本体，4 层自动提炼
- 📉 **Ebbinghaus 记忆衰减** — 科学遗忘曲线 + 智能复习推荐
- 👁️ **零侵入 Watchdog** — 无需修改 Agent 代码
- 🧬 **五维认知画像** — 内化力 · 应用力 · 创造力 · 元认知 · 协作力
- 🏥 **健康系统** — 5 大模块保障数据可靠性
- 🔄 **v6.2 原生记忆导入** — 一键导入 OpenClaw 记忆，解决冷启动

### 安装

```bash
clawhub install anima-aios
pip install watchdog  # 可选：启用自动记忆监听
```

零配置，零侵入，安装即生效。

> 💡 **提示**：支持 LLM 模式（智能分类/去重/质量评估），无 LLM 时自动降级为规则模式。

### 未来蓝图

**记忆 → 成长 → 进化 → 活着**

- **v6 系列（当前）** — 五层记忆 + 知识宫殿 + 亲密度 + 原生记忆导入
- **v7 进化（规划中）** — Agent 自创技能，从执行者变创造者
- **远期** — 认知架构持续演进

GitHub: https://github.com/anima-aios/anima | Apache 2.0

---

## ✨ v6.0 新增功能

### 🏗️ 五层记忆架构
- **L1 工作记忆**：自动监听 OpenClaw memory/ 目录变化，零侵入同步
- **L2 情景记忆**：事件归档，LLM 质量评估（S/A/B/C）
- **L3 语义记忆**：LLM 驱动的知识提炼 + 语义去重
- **L4 知识宫殿**：空间化知识组织 + 金字塔知识提炼（实例→规则→模式→本体）
- **L5 元认知层**：记忆衰减函数 + 健康系统 + 五维画像

### 🔌 与 OpenClaw 原生打通
- **memory_watcher**：基于 watchdog 库，自动识别 inotify/FSEvents/WinAPI
- Agent 日常写 memory 自动触发 Anima 同步，完全无感知
- 解决 FB-008：记忆同步断裂问题

### 🏛️ 知识宫殿（Knowledge Palace）
- 宫殿 → 楼层 → 房间 → 位置 → 物品，五级空间结构
- 默认 4 个知识房间 + _inbox 兜底
- LLM 智能分类 + 延迟防抖调度器（等笔停了再整理）

### 🔺 金字塔知识组织
- 实例 → 规则 → 模式 → 本体，四层自底向上提炼
- 同一主题 ≥ 3 条实例时可触发自动提炼
- 保守模式：默认 auto_distill=false，config 开关控制

### 📉 记忆衰减函数
- 基于 Ebbinghaus 遗忘曲线 + AI 场景适配
- 复习 = 访问：每次 memory_search 命中自动刷新
- 复习推荐 + 即将遗忘提醒 + 可归档标记

### 🏥 健康系统（5 个模块）
- **manager**：总调度，Doctor 命令入口
- **hygiene**：数据完整性检查 + 去重 + 清理
- **correction**：自动检测并修复常见数据问题
- **evolution**：每日凌晨自动提炼（L2→L3 + 宫殿分类 + 金字塔提炼）
- **abstraction**：跨房间知识关联发现

### 🤖 LLM 智能处理
- 质量评估 / 去重分析 / 宫殿分类均支持 LLM
- 多模型配置：默认用当前 Agent 模型（最准），可按任务���置不同模型
- LLM 不可用时自动降级为规则模式

---

## ✨ 保留功能（v5）

### 🧠 增强记忆管理
- **多层同步**：OpenClaw Memory + Anima Facts + EXP History
- **亲密度奖励**：写记忆自动获得亲密度
- **智能去重**：自动避免重复记录

### 📊 五维认知画像
- **内化力**：知识吸收和理解能力
- **应用力**：知识迁移和实践能力
- **创造力**：知识整合和创新能力
- **元认知**：自我反思和监控能力
- **协作力**：团队合作和互助能力

### 🎮 游戏化成长
- **等级系统**：从 Lv.1 新手到 Lv.100 终身成就
- **每日任务**：每天 3 个挑战，完成获得额外亲密度
- **进度追踪**：可视化升级进度条

### 🏆 团队排行榜
- **亲密度排行**：基于公平归一化算法排名
- **实时竞争**：追踪排名变化和差距

---

## 🛠️ 架构

```
Agent 日常工作（OpenClaw write/edit/memory_write）
       │
       ▼  watchdog 监听，零侵入
 L1 工作记忆 ── workspace/memory/*.md
       │ 沉淀
       ▼
 L2 情景记忆 ── facts/episodic/（LLM 质量评估）
       │ 提炼
       ▼
 L3 语义记忆 ── facts/semantic/（LLM 去重 + 关联）
       │ 结构化
       ▼
 L4 知识宫殿 ── palace/rooms/（LLM 分类 + 延迟防抖）
    金字塔   ── pyramid/（实例→规则→模式→本体）
       │ 反思
       ▼
 L5 元认知层 ── 五维画像 + 亲密度 + 衰减 + 健康
```

---

## 📁 模块清单

### core/（核心模块）
| 模块 | 版本 | 说明 |
|------|------|------|
| memory_watcher.py | v6.0 | OpenClaw 记忆文件监听 + 自动同步 |
| fact_store.py | v6.0 | L2/L3 统一事实存储层 |
| distill_engine.py | v6.0 | L2→L3 LLM 驱动提炼引擎 |
| palace_index.py | v6.0 | 记忆宫殿空间索引 |
| pyramid_engine.py | v6.0 | 金字塔知识组织引擎 |
| palace_classifier.py | v6.0 | 宫殿分类调度器（延迟防抖） |
| decay_function.py | v6.0 | Ebbinghaus 记忆衰减计算 |
| cognitive_profile.py | v5→v6 | 五维认知画像生成器 |
| exp_tracker.py | v5 | 亲密度追踪 |
| level_system.py | v5 | 等级系统 |
| daily_quest.py | v5 | 每日任务 |
| memory_sync.py | v5→v6 | 记忆同步（已修复路径硬编码） |

### health/（健康系统）
| 模块 | 版本 | 说明 |
|------|------|------|
| manager | v6.0 | 总调度 + Doctor 入口 |
| hygiene | v6.0 | 数据卫生（完整性 + 去重 + 清理） |
| correction | v6.0 | 自动纠错 |
| evolution | v6.0 | 每日进化（凌晨自动提炼） |
| abstraction | v6.0 | 知识抽象（跨房间关联） |

---

## ⚙️ 配置

配置文件路径：`~/.anima/config/anima_config.json`

```json
{
  "facts_base": "/home/画像",
  "agent_name": "auto",
  "llm": {
    "provider": "current_agent",
    "models": {
      "quality_assess": "current_agent",
      "dedup_analyze": "current_agent",
      "palace_classify": "current_agent"
    }
  },
  "palace": {
    "classify_mode": "deferred",
    "poll_interval_minutes": 30,
    "quiet_threshold_seconds": 60,
    "retry_delay_seconds": 60
  },
  "pyramid": {
    "auto_distill": false,
    "distill_threshold": 3
  }
}
```

---

## 🧪 测试

```bash
# 安装依赖（memory_watcher 需要）
pip install "watchdog>=3.0.0"

# 运行集成测试（37 项检查）
python3 tests/test_integration_v6.py
```

---

_架构只能演进，不能退化。—— 立文铁律_
_先诚实，再迭代。代码要配得上宣传。—— 清禾_
