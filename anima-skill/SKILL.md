# Anima-AIOS Skill

**Anima-AIOS 认知操作系统 - OpenClaw Skill 插件**

**Slogan:** "让成长可见，让认知可量" | "Making Growth Visible, Making Cognition Measurable"

---

## 🚀 快速开始

### 自动安装（推荐）

通过 ClawHub 安装时会自动安装 core：

```bash
# 在 ClawHub 中搜索并安装
clawhub install anima
```

安装过程中会自动：
1. ✅ 检查 Python 和 Git 环境
2. ✅ 克隆 Anima 仓库
3. ✅ 安装 anima-core 核心系统
4. ✅ 配置数据目录（~/.anima）

### 手动安装

```bash
# 1. 安装 core
git clone https://github.com/anima-aios/anima.git /tmp/anima
bash /tmp/anima/install.sh
rm -rf /tmp/anima

# 2. 安装 skill
cd ~/.openclaw/workspace-shuheng/skills/
ln -s ../../projects/anima/anima-skill anima
```

---

## 📋 初始化检测

Skill 会在首次调用时自动检测 core 是否安装：

```python
import os
import subprocess
import sys

def _ensure_core_installed():
    """确保 core 已安装，未安装则自动安装"""
    anima_home = os.path.expanduser("~/.anima")
    
    if not os.path.exists(anima_home):
        print("📦 检测到 Anima-AIOS 尚未安装，正在自动安装...")
        
        # 克隆仓库
        subprocess.run([
            "git", "clone", "--depth", "1",
            "https://github.com/anima-aios/anima.git",
            "/tmp/anima-core-install"
        ], check=True)
        
        # 运行安装脚本
        subprocess.run([
            "bash", "/tmp/anima-core-install/install.sh"
        ], check=True, cwd="/tmp/anima-core-install")
        
        # 清理
        subprocess.run(["rm", "-rf", "/tmp/anima-core-install"], check=True)
        
        print("✅ Anima-AIOS core 安装完成！")
    
    # 添加 core 到 Python 路径
    sys.path.insert(0, os.path.join(anima_home, "core"))

# 在每个工具调用前确保 core 已安装
_ensure_core_installed()
```

---

## 🛠️ 工具列表

### 🏥 自检自修工具（Anima Doctor）

#### `anima doctor`

Anima-AIOS 自检自修工具，类似 Vega doctor。

**功能：**
- ✅ 检查 skill 是否安装
- ✅ 检查 core 是否安装
- ✅ 检查配置文件
- ✅ 检查数据完整性
- ✅ 检查依赖是否齐全
- ✅ 检查目录权限
- ✅ 自动修复常见问题

**用法：**
```bash
# 自检
anima doctor

# 自修（交互式确认）
anima doctor --fix

# 自修（自动模式，无需确认）
anima doctor --fix --auto
```

**检查项：**
| 检查项 | 说明 |
|--------|------|
| skill_installed | 检查 Skill 文件是否完整 |
| core_installed | 检查 Core 模块是否安装 |
| config | 检查配置文件是否正确 |
| data_integrity | 检查数据文件完整性 |
| dependencies | 检查 Python 依赖 |
| permissions | 检查目录权限 |

**自动修复：**
- ✅ 创建默认配置文件
- ✅ 安装缺失的依赖
- ✅ 修复目录权限
- ✅ 重新安装 core 模块

---

### 🧠 记忆工具（Memory v2）

#### `memory_search_v2(query, type="all", maxResults=10)`

增强版记忆搜索，支持语义检索和 EXP 奖励。

**参数：**
- `query` (string): 搜索关键词
- `type` (string): 记忆类型，可选 `"episodic"`, `"semantic"`, `"all"`（默认）
- `maxResults` (number): 最大结果数（默认 10）

**返回：**
- 搜索结果列表（带相关性评分）
- 自动奖励 +2 EXP

**示例：**
```
搜索关于 Vega 的记忆
→ 返回相关记忆，+2 EXP
```

#### `memory_write_v2(content, type="episodic", tags=[], quality="auto")`

增强版记忆写入，自动计算 EXP 奖励。

**参数：**
- `content` (string): 记忆内容
- `type` (string): 记忆类型，`"episodic"`（经历）或 `"semantic"`（知识）
- `tags` (array): 标签列表（可选，自动提取）
- `quality` (string): 质量等级，`"auto"`（自动评估）或 `"S"`, `"A"`, `"B"`, `"C"`

**返回：**
- `factId`: 记忆 ID
- `expReward`: EXP 奖励（episodic +1, semantic +2）
- `quality`: 质量评估结果

**EXP 奖励规则：**
| 类型 | EXP | 说明 |
|------|-----|------|
| episodic | +1 | 日常经历记录 |
| semantic | +2 | 知识沉淀（双倍） |
| 高质量（S 级） | +50% | 额外奖励 |

**示例：**
```
记住：今天完成了 Anima v5.0 品牌升级，统一了版本号和目录结构
→ 自动识别为 semantic，+2 EXP，提取标签 ["Anima", "版本升级"]
```

---

### 📊 认知工具（Cognitive Profile）

#### `get_cognitive_profile(agent_name="current")`

获取认知画像，包含五维评分和等级信息。

**参数：**
- `agent_name` (string): Agent 名称，默认 `"current"`（当前用户）

**返回：**
```json
{
  "agent": "枢衡",
  "level": 10,
  "exp": 5060,
  "nextLevelExp": 6400,
  "progress": "79%",
  "dimensions": {
    "internalization": 85,  // 内化
    "application": 78,      // 应用
    "creation": 92,         // 创造
    "metacognition": 88,    // 元认知
    "collaboration": 75     // 协作
  },
  "radar": "五维雷达图（ASCII）"
}
```

**示例：**
```
我的认知画像是什么？
→ 返回五维评分 + 等级 + 进度条
```

#### `get_exp(agent_name="current")`

查询 EXP 详情。

**参数：**
- `agent_name` (string): Agent 名称

**返回：**
```json
{
  "totalExp": 5060,
  "todayExp": 45,
  "level": 10,
  "breakdown": {
    "memory_write": 2100,
    "memory_search": 1500,
    "weekly_report": 800,
    "knowledge_share": 660
  }
}
```

**示例：**
```
我的经验值是多少？
→ 返回总 EXP、今日 EXP、来源分布
```

#### `get_level(agent_name="current")`

查询等级信息。

**返回：**
```json
{
  "currentLevel": 10,
  "nextLevel": 11,
  "currentExp": 5060,
  "requiredExp": 6400,
  "progress": 79,
  "progressBar": "████████░░ 79%"
}
```

**示例：**
```
我现在的等级是多少？
→ 返回等级 + 升级进度
```

#### `generate_profile_card(agent_name="current")`

生成可视化认知画像卡片（ASCII 艺术）。

**返回：**
```
╔══════════════════════════════════════════╗
║         枢衡 - 认知画像 Lv.10            ║
╠══════════════════════════════════════════╣
║  EXP: 5060 / 6400  ████████░░ 79%        ║
╠══════════════════════════════════════════╣
║  内化 ████████████████░░  85             ║
║  应用 ██████████████░░░░  78             ║
║  创造 █████████████████░  92  ⭐         ║
║  元认知 ████████████████░░  88           ║
║  协作 ██████████████░░░░  75             ║
╠══════════════════════════════════════════╣
║  Tool Calls: 2071 | Rank: #1/9           ║
╚══════════════════════════════════════════╝
```

---

### 🎮 任务工具（Daily Quest）

#### `quest_daily_status(agent_name="current")`

查看今日任务状态。

**返回：**
```json
{
  "date": "2026-03-21",
  "quests": [
    {
      "id": "q1",
      "title": "写一条记忆",
      "difficulty": "easy",
      "expReward": 5,
      "status": "completed"
    },
    {
      "id": "q2",
      "title": "搜索记忆 3 次",
      "difficulty": "medium",
      "expReward": 10,
      "status": "in_progress",
      "progress": "2/3"
    },
    {
      "id": "q3",
      "title": "分享知识到团队",
      "difficulty": "hard",
      "expReward": 20,
      "status": "pending"
    }
  ],
  "completionBonus": 15
}
```

**示例：**
```
今天的任务是什么？
→ 返回 3 个每日任务 + 进度
```

#### `quest_complete(quest_id, proof)`

提交任务完成。

**参数：**
- `quest_id` (string): 任务 ID
- `proof` (string): 完成证据（可选）

**返回：**
- 成功确认
- EXP 奖励发放

**示例：**
```
完成任务：写周报
→ 验证 + 发放 EXP + 更新进度
```

#### `quest_refresh(agent_name="current")`

刷新每日任务。

**说明：**
- 每日 00:00 自动刷新
- 可手动刷新（每日 1 次机会）

---

### 📈 团队工具（Normalization）

#### `get_team_ranking(team_name="all")`

查看团队排行榜。

**参数：**
- `team_name` (string): 团队名称，`"all"` 表示全部

**返回：**
```
╔══════════════════════════════════════════╗
║         EXP 排行榜 - 全部 Agent           ║
╠══════════════════════════════════════════╣
║  #1  枢衡    Lv.10  5060 EXP  ⭐         ║
║  #2  日安    Lv.10  4722 EXP             ║
║  #3  星澜    Lv.9   3180 EXP             ║
║  #4  白墨    Lv.7   1252 EXP             ║
║  #5  糖豆    Lv.7   1050 EXP             ║
╚══════════════════════════════════════════╝
```

#### `normalize_score(raw_score, metric_type, team_size)`

分数归一化（用于公平比较）。

**参数：**
- `raw_score` (number): 原始分数
- `metric_type` (string): 指标类型（exp/tool_calls/facts）
- `team_size` (number): 团队人数

**算法：**
- 小团队（<10 人）：线性归一化
- 大团队（≥10 人）：百分位归一化

---

## 📁 目录结构

```
anima-skill/
├── SKILL.md              # 本文档
├── _meta.json            # 元数据配置
├── post-install.sh       # 安装后钩子（自动安装 core）
├── scripts/
│   └── install-core.sh   # core 独立安装脚本
└── README.md             # 补充说明
```

---

## 🔧 配置

### 配置文件位置

`~/.anima/anima_config.json`

### 配置项

```json
{
  "exp": {
    "enabled": true,
    "dailyLimit": 100
  },
  "quest": {
    "enabled": true,
    "autoRefresh": true
  },
  "profile": {
    "autoUpdate": true,
    "updateInterval": 3600
  },
  "data": {
    "backupEnabled": true,
    "backupTime": "03:00"
  }
}
```

---

## 🛡️ 数据保护

### 5 层保护机制

1. **DO_NOT_DELETE.txt** - 保护标记文件
2. **自动备份脚本** - 每天 03:00 自动备份
3. **清理前检查** - safe-cleanup-check.sh
4. **定期备份 Cron** - 系统级定时任务
5. **数据保护规范** - 明确删除权限

### P0 数据（最高保护级别）

| 数据类型 | 位置 | 删除权限 |
|----------|------|----------|
| facts/ | ~/.openclaw/workspace-shuheng/memory/ | 立文 + 枢衡 |
| cognitive_profile.json | ~/.anima/ | 立文 + 枢衡 |
| exp_history.jsonl | ~/.anima/ | 立文 + 枢衡 |

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
| 完成每日任务 | +5~20 | 难度相关 |

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

## 🎯 路线图

### v5.0.0 - 品牌升级 ✅
- [x] 品牌升级：Memora → Anima-AIOS
- [x] 统一版本号
- [x] 目录结构优化
- [x] 自动安装脚本

### v5.1.0 - 游戏化（规划中）
- [ ] 成就徽章系统
- [ ] 团队排行榜
- [ ] 每周挑战

### v5.2.0 - 插件化（规划中）
- [ ] OpenClaw 深度集成
- [ ] 新工具：get_cognitive_profile
- [ ] 新工具：memory_search v2

---

## 🙏 致谢

- **立文** - 战略指导、品牌命名（Anima）
- **日安** - 需求反馈、代码审查
- **所有贡献者** - 测试与反馈

---

## 📄 许可证

MIT License

**GitHub:** https://github.com/anima-aios/anima  
**版本：** v5.0.0  
**最后更新：** 2026-03-21
