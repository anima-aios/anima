# Anima-AIOS

**Anima AI Operating System**

**Slogan:** "Making Growth Visible, Making Cognition Measurable"  
**中文：** "让成长可见，让认知可量"

---

## 🎯 项目定位

Anima-AIOS 是一个**认知评估与成长追踪系统**，为 AI Agent 提供：

- 🧠 **五维认知评估** - 内化/应用/创造/元认知/协作
- 📊 **累积制等级系统** - EXP 只增不减，等级只升不降
- 📈 **成长可视化** - 纯文本可视化卡片，潜移默化
- 🛡️ **数据保护机制** - 5 层保护，确保安全

---

## 🚀 快速开始

### 安装

```bash
# 从 GitHub 克隆
git clone https://github.com/anima-aios/anima.git
cd anima/openclaw-plugin

# 安装
bash install.sh
```

### 初始化等级

```bash
# 扫描 OpenClaw session 记录，计算初始等级
python3 core/session_scanner.py
```

### 查看认知画像

```bash
# 生成认知画像
python3 core/cognitive_profile.py <Agent 名称>
```

---

## 📊 等级系统

### EXP 获取规则

| 行为 | EXP | 说明 |
|------|-----|------|
| 写 episodic fact | +1 | 日常记录 |
| 写 semantic fact | +2 | 知识沉淀（双倍） |
| 搜索记忆 | +2 | 主动检索 |
| 分享知识到 shared/ | +5 | 团队贡献 |
| 写周报/复盘 | +5 | 元认知 |
| 协作任务 | +3 | 团队合作 |

### 等级公式

```
level = max(1, int(exp ^ 0.28))
```

**等级需求：**
- 2 EXP → Lv.1（新手起步）
- 100 EXP → Lv.3（第 1 天）
- 1000 EXP → Lv.6（第 1 周）
- 1 万 EXP → Lv.13（第 1 月）
- 10 万 EXP → Lv.25（第 1 年）
- 1400 万 EXP → Lv.100（终身成就）

---

## 📁 项目结构

```
anima-core/
├── core/
│   ├── normalization_engine.py    # 归一化引擎
│   ├── dimension_calculator.py    # 维度计算器
│   ├── cognitive_profile.py       # 认知画像生成器
│   ├── exp_tracker.py             # EXP 追踪器
│   ├── level_system.py            # 等级系统
│   ├── session_scanner.py         # Session 扫描器
│   ├── team_scanner.py            # 团队扫描器
│   ├── profile_card.py            # 画像卡片生成器
│   └── daily_quest.py             # 每日任务系统
├── scripts/
│   ├── protect-data.sh            # 数据保护脚本
│   ├── safe-cleanup-check.sh      # 清理检查脚本
│   └── ...
├── docs/
│   ├── DATA_PROTECTION.md         # 数据保护规范
│   └── ...
├── tests/
│   └── ...
└── README.md
```

---

## 🛡️ 数据保护

### 5 层保护机制

1. **DO_NOT_DELETE.txt** - 保护标记
2. **自动备份脚本** - protect-data.sh
3. **清理前检查** - safe-cleanup-check.sh
4. **定期备份 Cron** - 每天 03:00
5. **数据保护规范** - DATA_PROTECTION.md

### P0 数据（最高保护级别）

| 数据类型 | 删除权限 |
|----------|----------|
| facts/ | 立文 + 枢衡 |
| cognitive_profile.json | 立文 + 枢衡 |
| exp_history.jsonl | 立文 + 枢衡 |

---

## 📈 当前等级分布

| Agent | EXP | 等级 | Tool Calls |
|-------|-----|------|------------|
| **枢衡** | 5060 | **Lv.10** | 2071 |
| **日安** | 4722 | **Lv.10** | 1909 |
| **星澜** | 3180 | **Lv.9** | 1307 |
| **白墨** | 1252 | **Lv.7** | 540 |
| **糖豆** | 1050 | **Lv.7** | 451 |
| **流萤** | 470 | **Lv.5** | 213 |
| **正言** | 288 | **Lv.4** | 123 |
| **明澈** | 240 | **Lv.4** | 101 |
| **瑾瑜** | 223 | **Lv.4** | 91 |

---

## 📚 文档

- [数据保护规范](docs/DATA_PROTECTION.md)
- [变更日志](CHANGELOG.md)
- [发布说明](RELEASE_v4.0.5.md)

---

## 🎯 路线图

### v5.0.0 - 品牌升级
- [x] 品牌升级：Memora → Anima-AIOS
- [ ] 更新所有文档
- [ ] 发布 GitHub Release
- [ ] 开源公告

### v5.1.0 - 游戏化
- [ ] 成就徽章系统
- [ ] 团队排行榜
- [ ] 每日挑战任务

### v5.2.0 - 插件化
- [ ] OpenClaw 插件集成
- [ ] 新工具：get_cognitive_profile
- [ ] 新工具：memory_search v2

---

## 🙏 致谢

- **立文** - 战略指导、品牌命名
- **日安** - 需求反馈
- **所有贡献者** - 测试与反馈

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

**Anima-AIOS — Making Growth Visible, Making Cognition Measurable**

**GitHub:** https://github.com/anima-aios/anima  
**版本：** v5.0.0 (品牌升级版)
