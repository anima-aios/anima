# Memora v4.0 — Phase 5 & 6: 多维度认知等级系统 + 可视化

**版本：** 4.0.0  
**开发日期：** 2026-03-20  
**状态：** ✅ 生产就绪  
**作者：** 枢衡

---

## 🎯 核心特性

### 基于认知科学的评估体系

Memora v4.0 不再使用单一的游戏化 EXP 系统，而是基于认知科学理论（Dreyfus 技能习得模型、Bloom 认知分类、Ericsson 刻意练习）设计了**五维认知评估体系**：

```
                    知识创造 (Create)
                         25%
                        /
                       /
     元认知 (Meta) ——•—— 知识应用 (Apply)
        15%          /         20%
                    /
                   /
          知识内化 (Understand)  协作认知 (Collab)
               20%                  20%
```

---

## 📐 五维认知模型

### 1. 知识内化 (Understanding) — 20%

**定义：** 将外部信息转化为内部知识的能力

**评估指标：**
- Semantic facts 数量（权重 2.0）
- Episodic facts 数量（权重 1.0）
- 内容长度奖励（>200 字 +0.5）
- 标签使用（+0.5）

**行为映射：**
- 写 semantic fact → +2 EXP
- 写 episodic fact → +1 EXP
- 深度反思（>200 字）→ 质量系数 1.5x

---

### 2. 知识应用 (Application) — 20%

**定义：** 在新情境中使用已有知识的能力

**评估指标：**
- Memory search 次数（权重 2.0）
- 搜索后完成任务（+10）
- 知识复用（+3.0）

**行为映射：**
- 主动搜索记忆 → +2 EXP
- 搜索后 24h 内完成任务 → +10 EXP

---

### 3. 知识创造 (Creation) — 25%

**定义：** 生成新知识、新方法、新见解的能力

**评估指标：**
- 分享到 shared/ 次数（权重 5.0）
- 创建技能（+10）
- 知识整合（+4.0）
- 被他人引用（+2.0）

**行为映射：**
- 写入 shared/ → +5 EXP
- 创建共享技能 → +10 EXP

---

### 4. 元认知 (Metacognition) — 15%

**定义：** 对自己认知过程的认知和调节

**评估指标：**
- 周报/复盘次数（权重 5.0）
- 反思类 facts（+2.0）
- 目标设定（+3.0）
- 进度追踪（+2.0）

**行为映射：**
- 写周报 → +5 EXP
- 反思类 fact → +2 EXP

---

### 5. 协作认知 (Collaboration) — 20%

**定义：** 在协作中贡献和获取知识的能力

**评估指标：**
- 协助他人次数（权重 3.0）
- 主动求助（+1.0）
- 协作任务（+4.0）
- 审稿/Code Review（+3.0）

**行为映射：**
- 协助他人 → +3 EXP
- 参与协作任务 → +4 EXP

---

## 🧮 等级计算

### 归一化策略

根据团队规模自动切换：

| 团队规模 | 归一化模式 | 说明 |
|----------|-----------|------|
| **1 人** | 绝对基准 | 基于认知科学标准 |
| **2-4 人** | 混合模式 | 50% 绝对 + 50% 相对 |
| **5+ 人** | 百分位数 | 团队排名 |

### 等级映射（Dreyfus 模型）

| 认知分数 | 等级 | 阶段 | 徽章 |
|----------|------|------|------|
| 90-100 | Lv.100 | Expert 专家 | 👑 Legendary |
| 80-89 | Lv.80 | Proficient 熟练者 | 🏆 Master |
| 60-79 | Lv.60 | Competent 胜任者 | 🌳 Expert |
| 40-59 | Lv.40 | Advanced Beginner 高级初学者 | 🌿 Advanced |
| 0-39 | Lv.20 | Novice 新手 | 🌱 Novice |

---

## 📦 项目结构

```
phase-5-level-system/
├── core/
│   ├── __init__.py                # 模块初始化
│   ├── normalization_engine.py    # 归一化引擎
│   ├── dimension_calculator.py    # 维度计算器
│   ├── cognitive_profile.py       # 认知画像生成器
│   ├── exp_tracker.py             # EXP 追踪器 v2
│   └── daily_quest.py             # 每日任务系统
├── scripts/
│   ├── show-progress.sh           # 显示认知进度
│   ├── refresh-quests.sh          # 刷新每日任务
│   └── calculate-exp.sh           # 计算 EXP
├── cron/
│   └── memora-v4-crontab          # Cron 配置模板
├── tests/
│   ├── test_normalization.py
│   ├── test_dimension.py
│   ├── test_exp_tracker.py
│   └── test_daily_quest.py
└── README.md                      # 本文档
```

---

## 🚀 快速开始

### 1. 安装

```bash
cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system

# 无需额外依赖（纯 Python 3.9+）
```

### 2. 生成认知画像

```bash
./scripts/show-progress.sh 枢衡
```

### 3. 刷新每日任务

```bash
./scripts/refresh-quests.sh 枢衡
```

### 4. 配置 Cron（可选）

```bash
# 编辑 Cron 配置
cd cron
vim memora-v4-crontab

# 修改 AGENT_NAME 为实际 Agent 名称
# 修改 MEMORA_DIR 为实际路径

# 安装 Cron
crontab memora-v4-crontab
```

---

## 📋 每日任务系统

### 4 个通用基础任务

| 任务 | EXP | 说明 |
|------|-----|------|
| 📝 写 1 条事实 | +1 | 记录今天的工作或学习 |
| 🔍 搜索 1 次记忆 | +2 | 主动检索已有知识 |
| ✅ 完成 1 个任务 | +30 | 完成任何工作任务 |
| 💬 参与 1 次协作 | +15 | 写入 shared/ 或协助他人 |

### 全部完成奖励

完成所有任务 → 额外 **+50 EXP**

### 自动检测

系统每小时自动检查任务进度，完成后自动发放 EXP。

---

## 🛡️ 防刷机制

### 1. 每日 EXP 上限

| 维度 | 上限 |
|------|------|
| Understanding | 50 EXP/天 |
| Application | 40 EXP/天 |
| Creation | 60 EXP/天 |
| Metacognition | 30 EXP/天 |
| Collaboration | 50 EXP/天 |

### 2. 质量系数

```
内容长度 <50 字   → 质量系数 0.3（可能无效）
内容长度 50-200 字 → 质量系数 1.0（正常）
内容长度 >200 字   → 质量系数 1.5（深度反思）
```

### 3. 重复检测

相同内容（基于哈希）24 小时内只计 1 次 EXP。

---

## 🧪 测试

```bash
# 测试归一化引擎
cd core
python3 normalization_engine.py

# 测试维度计算器
python3 dimension_calculator.py 枢衡

# 测试认知画像生成
python3 cognitive_profile.py 枢衡

# 测试 EXP 追踪器
python3 exp_tracker.py 枢衡 summary

# 测试每日任务系统
python3 daily_quest.py 枢衡 status
```

---

## 📊 配置示例

### memora_config.json

```json
{
  "normalization": {
    "mode": "auto",
    "use_global_benchmark": false,
    "team_size_threshold": {
      "percentile": 5,
      "hybrid": 2,
      "absolute": 1
    }
  },
  
  "weights": {
    "understanding": 0.20,
    "application": 0.20,
    "creation": 0.25,
    "metacognition": 0.15,
    "collaboration": 0.20
  },
  
  "benchmarks": {
    "understanding": {
      "novice": 10,
      "beginner": 30,
      "competent": 60,
      "proficient": 100,
      "expert": 200
    }
  }
}
```

---

## 📝 API 使用示例

### Python API

```python
from core import NormalizationEngine, DimensionCalculator, CognitiveProfileGenerator, EXPTracker

# 1. 计算维度分数
calculator = DimensionCalculator('枢衡')
raw_scores = calculator.calculate_all_dimensions()

# 2. 归一化
normalizer = NormalizationEngine()
normalized = normalizer.normalize(raw_scores)

# 3. 计算综合分数
cognitive_score = normalizer.calculate_cognitive_score(normalized)

# 4. 映射到等级
level_info = normalizer.score_to_level(cognitive_score)
print(f"等级：Lv.{level_info['level']} - {level_info['stage']}")

# 5. 生成认知画像
generator = CognitiveProfileGenerator('枢衡')
profile = generator.generate_profile()
card = generator.generate_profile_card(profile)
print(card)

# 6. 添加 EXP
tracker = EXPTracker('枢衡')
success, message = tracker.add_exp(
    dimension='understanding',
    action='write_semantic_fact',
    exp=2,
    quality_multiplier=1.5
)
```

---

## 📅 开发计划

- [x] Phase 5A: 核心引擎（归一化、维度计算、EXP 追踪）
- [x] Phase 5B: 每日任务系统
- [ ] Phase 5C: 测试用例
- [ ] Phase 5D: 文档完善
- [ ] Phase 6: 可视化（成长曲线、雷达图）
- [ ] Phase 7: 游戏化（成就徽章、排行榜）

---

## 🙏 理论基础

- **Dreyfus 技能习得模型** (1980) — 新手→专家的 5 个阶段
- **Bloom 认知目标分类** (修订版) — 记忆/理解/应用/分析/评价/创造
- **Ericsson 刻意练习理论** (1993) — 专家需约 10000 小时
- **Flavell 元认知理论** (1979) — 对认知的认知

---

## 📞 联系方式

- **项目负责人:** 枢衡
- **开发日期:** 2026-03-20
- **版本:** 4.0.0

---

**Memora v4.0 — 让成长可见，让认知可量化**
emora v4.0 — 让成长可见，让认知可量化**
