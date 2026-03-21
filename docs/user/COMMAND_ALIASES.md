# Anima-AIOS 指令别名对照表

**版本：** v5.0.3  
**最后更新：** 2026-03-22  
**语言支持：** ✅ 中文 + ✅ 英文

---

## 🎯 认知画像指令

### 主指令
- `get_cognitive_profile(agent_name="current")`

### 支持的别名（中英文）

| 中文指令 | English Command | 功能 |
|---------|----------------|------|
| **我的认知画像是什么？** | **What is my cognitive profile?** | 主指令 |
| 角色面板 | Character panel | ✅ 同认知画像 |
| 人物面板 | Profile panel | ✅ 同认知画像 |
| 属性界面 | Attributes screen | ✅ 同认知画像 |
| 个人信息 | Personal info | ✅ 同认知画像 |
| 人物画像 | Character profile | ✅ 同认知画像 |
| 我的属性 | My attributes | ✅ 同认知画像 |
| 我的能力 | My abilities | ✅ 同认知画像 |
| 我的五维评分 | My five dimensions | ✅ 同认知画像 |
| 我的雷达图 | My radar chart | ✅ 同认知画像 |

### 使用示例

**中文：**
```
用户：角色面板
Anima: ╔══════════════════════════════════════════╗
       ║         枢衡 - 认知画像 Lv.11            ║
       ╠══════════════════════════════════════════╣
       ║  EXP: 5,266 / 7,148  ████████░░  73%     ║
       ╚══════════════════════════════════════════╝

用户：属性界面
Anima: [显示五维评分和等级信息]

用户：个人信息
Anima: [显示个人信息和成长进度]
```

**English：**
```
User: Character panel
Anima: ╔══════════════════════════════════════════╗
       ║         Shuheng - Cognitive Profile      ║
       ║                    Lv.11                 ║
       ╠══════════════════════════════════════════╣
       ║  EXP: 5,266 / 7,148  ████████░░  73%     ║
       ╚══════════════════════════════════════════╝

User: Attributes screen
Anima: [Show five dimensions and level info]

User: Personal info
Anima: [Show personal info and growth progress]
```

---

## 📝 记忆管理指令

### 主指令
- `memory_write_v2(content, type="episodic", tags=[], quality="auto")`
- `memory_search_v2(query, type="all", maxResults=10)`

### 支持的别名

| 中文指令 | English Command | 功能 |
|---------|----------------|------|
| **记住：[内容]** | **Remember: [content]** | 写入记忆 |
| 记一下：[内容] | Note this: [content] | ✅ 同写入记忆 |
| 记录：[内容] | Record: [content] | ✅ 同写入记忆 |
| 搜索关于 [关键词] 的记忆 | Search memories about [keyword] | ✅ 搜索记忆 |
| 查找 [关键词] | Find [keyword] | ✅ 搜索记忆 |
| 我的记忆 | My memories | ✅ 查看记忆列表 |

---

## 📊 EXP 查询指令

### 主指令
- `get_exp(agent_name="current")`

### 支持的别名

| 中文指令 | English Command | 功能 |
|---------|----------------|------|
| **我的经验值是多少？** | **How much EXP do I have?** | 主指令 |
| 我有多少 EXP | How much EXP do I have | ✅ 同 EXP 查询 |
| 我的成长进度 | My growth progress | ✅ 同 EXP 查询 |
| 我的 EXP | My EXP | ✅ 同 EXP 查询 |

---

## 🎯 等级查询指令

### 主指令
- `get_level(agent_name="current")`

### 支持的别名

| 中文指令 | English Command | 功能 |
|---------|----------------|------|
| **我现在的等级是多少？** | **What is my current level?** | 主指令 |
| 我离升级还有多远 | How far to next level | ✅ 同等级查询 |
| 下一级需要多少 EXP | How much EXP for next level | ✅ 同等级查询 |
| 我的等级 | My level | ✅ 同等级查询 |

---

## 📋 每日任务指令

### 主指令
- `quest_daily_status(agent_name="current")`
- `quest_complete(quest_id, proof=None)`

### 支持的别名

| 中文指令 | English Command | 功能 |
|---------|----------------|------|
| **今天的任务是什么？** | **What are today's tasks?** | 主指令 |
| 完成任务：[任务名] | Complete task: [task name] | ✅ 提交任务 |
| 我的任务进度 | My task progress | ✅ 查看进度 |
| 今日任务 | Today's tasks | ✅ 同每日任务 |

---

## 🏆 团队排行指令

### 主指令
- `get_team_ranking(team_name="all")`

### 支持的别名

| 中文指令 | English Command | 功能 |
|---------|----------------|------|
| **查看团队排行榜** | **Show team leaderboard** | 主指令 |
| 我的排名 | My ranking | ✅ 查看个人排名 |
| 谁排第一 | Who is #1 | ✅ 查看第一名 |
| 团队排名 | Team ranking | ✅ 同排行榜 |

---

## 🏥 自检自修指令

### 主指令
- `anima doctor`
- `anima doctor --fix`
- `anima doctor --fix --auto`

### 支持的别名

| 中文指令 | English Command | 功能 |
|---------|----------------|------|
| **anima doctor** | **anima doctor** | 通用指令 |
| 检查 Anima 状态 | Check Anima status | ✅ 同自检 |
| 修复 Anima | Fix Anima | ✅ 同自修 |
| Anima 自检 | Anima self-check | ✅ 同自检 |

---

## 🌐 语言自动识别

Anima 会自动识别用户使用的语言，并用相同语言回复：

```
用户（中文）：角色面板
Anima（中文）：╔══════════════════════════════════════════╗
              ║         枢衡 - 认知画像 Lv.11            ║
              ╚══════════════════════════════════════════╝

用户（英文）：Character panel
Anima（英文）：╔══════════════════════════════════════════╗
              ║         Shuheng - Cognitive Profile      ║
              ║                    Lv.11                 ║
              ╚══════════════════════════════════════════╝
```

---

## 📊 指令统计

| 类别 | 主指令数 | 别名数 | 语言支持 |
|------|---------|--------|---------|
| 认知画像 | 1 | 10+ | ✅ 中英文 |
| 记忆管理 | 2 | 6+ | ✅ 中英文 |
| EXP 查询 | 1 | 4+ | ✅ 中英文 |
| 等级查询 | 1 | 4+ | ✅ 中英文 |
| 每日任务 | 2 | 4+ | ✅ 中英文 |
| 团队排行 | 1 | 4+ | ✅ 中英文 |
| 自检自修 | 3 | 3+ | ✅ 通用 |

**总计：** 11 个主指令，35+ 个别名

---

## 🎯 最佳实践

### 1. 使用自然语言

**推荐：**
```
记住：今天发布了 Anima v5.0.3
我的认知画像是什么？
今天的任务是什么？
```

**不推荐：**
```
memory_write_v2(content="...", type="episodic")
get_cognitive_profile(agent_name="current")
quest_daily_status(agent_name="current")
```

### 2. 中英文混用

Anima 支持中英文混用：
```
用户：Remember 今天发布了 Anima
用户：我的 cognitive profile 是什么？
用户：Complete task 写工作日志
```

### 3. 简洁指令

**简洁：**
```
角色面板
属性界面
个人信息
```

**完整：**
```
我的认知画像是什么？
查看我的属性界面
显示我的个人信息
```

---

## 📚 相关文档

| 文档 | 说明 | 路径 |
|------|------|------|
| [使用手册](USAGE.md) | 详细使用教程 | docs/user/USAGE.md |
| [使用示例](EXAMPLES.md) | 实际使用案例 | docs/user/EXAMPLES.md |
| [游戏化功能](GAME_FEATURES.md) | 游戏化机制介绍 | docs/user/GAME_FEATURES.md |

---

**维护者：** 枢衡  
**最后更新：** 2026-03-22  
**版本：** v5.0.3
