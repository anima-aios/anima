# Anima-AIOS 使用指令总结

**版本：** v5.0.3  
**最后更新：** 2026-03-22  
**语言支持：** ✅ 中文 + ✅ 英文

---

## 🎯 核心使用指令

### 1. 记忆管理

| 指令（中文） | Command (English) | 功能 |
|------------|------------------|------|
| `记住：[内容]` | `Remember: [content]` | 写入记忆 |
| `搜索关于 [关键词] 的记忆` | `Search memories about [keyword]` | 搜索记忆 |
| `我的记忆` | `My memories` | 查看记忆列表 |

**示例：**
```
中文：记住：今天完成了 Anima v5.0.3 发布
英文：Remember: Completed Anima v5.0.3 release today

中文：搜索关于 Vega 的记忆
英文：Search memories about Vega
```

---

### 2. 认知画像

| 指令（中文） | Command (English) | 功能 |
|------------|------------------|------|
| `我的认知画像是什么？` | `What is my cognitive profile?` | 查看认知画像 |
| `我的能力分布` | `My ability distribution` | 查看五维评分 |
| `我的等级` | `My level` | 查看等级信息 |

**示例：**
```
中文：我的认知画像是什么？
英文：What is my cognitive profile?

中文：我的能力分布
英文：My ability distribution
```

---

### 3. EXP 查询

| 指令（中文） | Command (English) | 功能 |
|------------|------------------|------|
| `我的经验值是多少？` | `How much EXP do I have?` | 查看 EXP |
| `我有多少 EXP` | `How much EXP do I have` | 查看 EXP（简写） |
| `我的成长进度` | `My growth progress` | 查看成长进度 |

**示例：**
```
中文：我的经验值是多少？
英文：How much EXP do I have?
```

---

### 4. 等级查询

| 指令（中文） | Command (English) | 功能 |
|------------|------------------|------|
| `我现在的等级是多少？` | `What is my current level?` | 查看等级 |
| `我离升级还有多远` | `How far to next level` | 查看升级进度 |
| `下一级需要多少 EXP` | `How much EXP for next level` | 查看升级需求 |

**示例：**
```
中文：我现在的等级是多少？
英文：What is my current level?

中文：我离升级还有多远
英文：How far to next level
```

---

### 5. 每日任务

| 指令（中文） | Command (English) | 功能 |
|------------|------------------|------|
| `今天的任务是什么？` | `What are today's tasks?` | 查看每日任务 |
| `完成任务：[任务名]` | `Complete task: [task name]` | 提交任务完成 |
| `我的任务进度` | `My task progress` | 查看任务进度 |

**示例：**
```
中文：今天的任务是什么？
英文：What are today's tasks?

中文：完成任务：写工作日志
英文：Complete task: Write work log
```

---

### 6. 团队排行

| 指令（中文） | Command (English) | 功能 |
|------------|------------------|------|
| `查看团队排行榜` | `Show team leaderboard` | 查看团队排行 |
| `我的排名` | `My ranking` | 查看个人排名 |
| `谁排第一` | `Who is #1` | 查看第一名 |

**示例：**
```
中文：查看团队排行榜
英文：Show team leaderboard

中文：我的排名
英文：My ranking
```

---

### 7. 自检自修

| 指令（中文） | Command (English) | 功能 |
|------------|------------------|------|
| `anima doctor` | `anima doctor` | 自检（通用） |
| `anima doctor --fix` | `anima doctor --fix` | 自修（通用） |
| `检查 Anima 状态` | `Check Anima status` | 检查状态 |

**示例：**
```
中文：anima doctor
英文：anima doctor

中文：anima doctor --fix
英文：anima doctor --fix
```

---

## 📊 EXP 奖励规则

### 记忆写入

| 类型 | C/B 级 | A 级 | S 级 |
|------|--------|-----|-----|
| **episodic** | +1 EXP | +2 EXP | +2 EXP |
| **semantic** | +2 EXP | +3 EXP | +3 EXP |

### 任务完成

| 难度 | EXP 奖励 |
|------|---------|
| **简单** | +5 EXP |
| **中等** | +10 EXP |
| **困难** | +15-20 EXP |
| **全部完成** | +15 EXP（额外） |

### 其他操作

| 操作 | EXP 奖励 |
|------|---------|
| **搜索记忆** | +2 EXP/次 |
| **分享知识** | +5 EXP/次 |
| **写周报** | +5 EXP/次 |

---

## 🌐 语言兼容性

### ✅ 已支持的语言

| 语言 | 状态 | 示例 |
|------|------|------|
| **中文** | ✅ 完全支持 | 记住、搜索、我的认知画像 |
| **英文** | ✅ 完全支持 | Remember, Search, My cognitive profile |
| **混合** | ✅ 支持 | 记住：Remember this |

### 🔄 自动识别

Anima 会自动识别用户使用的语言，并用相同语言回复：

```
用户（中文）：我的经验值是多少？
Anima（中文）：你的经验值是 5,266 EXP...

用户（英文）：How much EXP do I have?
Anima（英文）：You have 5,266 EXP...
```

---

## 📝 完整使用流程示例

### 中文流程

```
1. 用户：记住：今天发布了 Anima v5.0.3
   Anima: ✅ 记忆已保存，+1 EXP（episodic, C 级）

2. 用户：我的认知画像是什么？
   Anima: ╔══════════════════════════════════════════╗
          ║         枢衡 - 认知画像 Lv.11            ║
          ╠══════════════════════════════════════════╣
          ║  EXP: 5,266 / 7,148  ████████░░  73%     ║
          ╚══════════════════════════════════════════╝

3. 用户：今天的任务是什么？
   Anima: 📅 今日任务 (2026-03-22)
          1. ⏳ 完成一次代码提交 (中等) +10 EXP
          2. ⏳ 写工作日志 (简单) +5 EXP
          3. ⏳ 搜索记忆 3 次 (中等) +10 EXP

4. 用户：完成任务：写工作日志
   Anima: ✅ 任务完成！+5 EXP
          今日任务进度：1/3
```

### English Workflow

```
1. User: Remember: Released Anima v5.0.3 today
   Anima: ✅ Memory saved, +1 EXP (episodic, C级)

2. User: What is my cognitive profile?
   Anima: ╔══════════════════════════════════════════╗
          ║         Shuheng - Cognitive Profile      ║
          ║                    Lv.11                 ║
          ╠══════════════════════════════════════════╣
          ║  EXP: 5,266 / 7,148  ████████░░  73%     ║
          ╚══════════════════════════════════════════╝

3. User: What are today's tasks?
   Anima: 📅 Today's Tasks (2026-03-22)
          1. ⏳ Complete a code commit (Medium) +10 EXP
          2. ⏳ Write work log (Easy) +5 EXP
          3. ⏳ Search memories 3 times (Medium) +10 EXP

4. User: Complete task: Write work log
   Anima: ✅ Task completed! +5 EXP
          Today's progress: 1/3
```

---

## 🔧 高级指令

### 命令行工具

```bash
# 自检
anima doctor

# 自修
anima doctor --fix

# 自动修复（无需确认）
anima doctor --fix --auto

# 同步记忆
/root/.openclaw/workspace/anima-core/scripts/sync-memory.sh
```

### OpenClaw 对话

```
# 查看帮助
Anima 有哪些功能？

# 查看版本
Anima 的版本是多少？

# 查看文档
Anima 的文档在哪里？
```

---

## 📚 相关文档

| 文档 | 说明 | 路径 |
|------|------|------|
| [使用手册](docs/user/USAGE.md) | 详细使用教程 | docs/user/USAGE.md |
| [使用示例](docs/user/EXAMPLES.md) | 实际使用案例 | docs/user/EXAMPLES.md |
| [游戏化功能](docs/user/GAME_FEATURES.md) | 游戏化机制介绍 | docs/user/GAME_FEATURES.md |
| [记忆同步指南](docs/MEMORY_SYNC_GUIDE.md) | 三层同步机制详解 | docs/MEMORY_SYNC_GUIDE.md |

---

**维护者：** 枢衡  
**最后更新：** 2026-03-22  
**版本：** v5.0.3
