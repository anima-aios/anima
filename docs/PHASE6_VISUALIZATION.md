# Memora v4.0 Phase 6 — 可视化设计

**版本：** 4.0.0 Phase 6  
**日期：** 2026-03-20  
**设计理念：** 潜移默化，不浮夸

---

## 🎯 设计原则

1. **极简主义** — 纯文本/Unicode，无需依赖
2. **一目了然** — 适合每日快速查看
3. **潜移默化** — 不是表演式的展示，而是安静的陪伴
4. **终端友好** — Markdown、飞书、微信都能直接显示

---

## 📊 可视化类型

### 1. 完整认知画像卡片

**用途：** 首次查看、周报生成

**示例：**
```
🧠 认知画像 — 枢衡

Lv.60 🌳 Expert Competent 胜任者
[██████░░░░] 74.8/100

━━━ 五维评估 ━━━

💡 知识创造     ████████░░  88.0 (#1)
🤝 协作认知     ███████░░░  81.0 (#2)
📚 知识内化     ███████░░░  72.0 (#3)
🔧 知识应用     ██████░░░░  65.0 (#5)
🤔 元认知      █████░░░░░  58.0 (#4)

━━━ 统计 ━━━

📝 总 Facts:    156
   ├─ Semantic: 45
   └─ Episodic: 111
🔍 记忆搜索：  89
📤 知识分享：  23
📊 周报复盘：  8
🤝 协作任务：  15

━━━━━━━━━━━━━━
生成时间：2026-03-20
```

---

### 2. 简化版卡片（每日查看）

**用途：** 每日任务完成后的快速反馈

**示例：**
```
🧠 枢衡 | Lv.60 🌳 | 74.8/100

知识创造   ████████░░  88.0
协作认知   ███████░░░  81.0
知识内化   ███████░░░  72.0
知识应用   ██████░░░░  65.0
元认知    █████░░░░░  58.0
```

---

### 3. 团队对比卡片

**用途：** 团队周报、月度总结

**示例：**
```
🏆 团队认知排名

排名 Agent        等级     分数   趋势
──────────────────────────────────────────
🥇   枢衡         Lv.60   74.8   📈 +3.2
🥈   明澈         Lv.55   68.2   📈 +1.5
🥉   流萤         Lv.50   62.5   ➡️ 0.0
#4   糖豆         Lv.45   58.3   📉 -0.8
#5   白墨         Lv.42   55.1   📈 +2.1

总计 5 个 Agent
```

---

## 🔧 技术实现

### 纯文本渲染

**进度条生成：**
```python
def generate_bar(score, max_length=10):
    """生成分数进度条"""
    bar_length = int(score / (100 / max_length))
    bar = '█' * bar_length + '░' * (max_length - bar_length)
    return bar
```

**排名图标：**
```python
RANK_ICONS = {
    1: '🥇',
    2: '🥈',
    3: '🥉',
}

def get_rank_icon(rank):
    return RANK_ICONS.get(rank, f'#{rank}')
```

---

### 自动团队扫描

**核心逻辑：**
```python
from team_scanner import TeamScanner

scanner = TeamScanner(active_days=30)
active_agents = scanner.scan_active_agents()

# 自动判断归一化模式
if len(active_agents) >= 5:
    mode = 'percentile'  # 大团队
elif len(active_agents) >= 2:
    mode = 'hybrid'      # 小团队
else:
    mode = 'absolute'    # 单 Agent
```

**活跃度判断：**
- 检查 facts 目录（episodic/semantic）
- 检查 exp_history.jsonl
- 检查 daily_quests 目录
- 检查 cognitive_profile.json

**默认窗口：** 30 天

---

## 📝 使用示例

### 1. 生成完整画像

```bash
cd core
python3 profile_card.py 枢衡
```

### 2. 生成简化版

```bash
python3 profile_card.py 枢衡 simple
```

### 3. 生成团队对比

```bash
python3 profile_card.py 枢衡 comparison
```

### 4. Python API

```python
from core import CognitiveProfileGenerator, ProfileCardGenerator

# 生成画像
profile_gen = CognitiveProfileGenerator('枢衡')
profile = profile_gen.generate_profile(auto_scan=True)

# 生成卡片
card_gen = ProfileCardGenerator()

# 完整版
full_card = card_gen.generate_card(profile)
print(full_card)

# 简化版
simple_card = card_gen.generate_simple_card(profile)
print(simple_card)
```

---

## 🎨 视觉元素

### 进度条字符

| 字符 | Unicode | 用途 |
|------|---------|------|
| █ | U+2588 | 已完成 |
| ░ | U+2591 | 未完成 |
| ─ | U+2500 | 分隔线 |
| │ | U+2502 | 垂直分隔 |

### 图标

| 维度 | 图标 | 含义 |
|------|------|------|
| 知识创造 | 💡 | 灵感、创新 |
| 协作认知 | 🤝 | 合作、协助 |
| 知识内化 | 📚 | 学习、吸收 |
| 知识应用 | 🔧 | 实践、使用 |
| 元认知 | 🤔 | 反思、思考 |

### 等级徽章

| 等级 | 徽章 | 阶段 |
|------|------|------|
| Lv.100 | 👑 | Expert 专家 |
| Lv.80 | 🏆 | Proficient 熟练者 |
| Lv.60 | 🌳 | Competent 胜任者 |
| Lv.40 | 🌿 | Advanced Beginner |
| Lv.20 | 🌱 | Novice 新手 |

---

## 🚀 未来增强（可选）

### Phase 6 Plus

- [ ] 生成 PNG 图片（matplotlib）
- [ ] HTML 交互式报告
- [ ] 导出 PDF

**原则：** 保持纯文本为核心，图片为可选增强

---

## 📞 联系方式

- **负责人:** 枢衡
- **日期:** 2026-03-20

---

**Memora v4.0 Phase 6 — 潜移默化，静待花开**
