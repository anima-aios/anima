# Anima-AIOS 记忆同步指南

**版本：** v5.0.2  
**最后更新：** 2026-03-21  
**状态：** ✅ 已实现

---

## 📊 问题背景

Anima 存在两套记忆系统：

1. **OpenClaw 记忆** - `/root/.openclaw/workspace-shuheng/memory/`
   - OpenClaw 默认记忆路径
   - 所有 Agent 共享

2. **Anima 记忆** - `/home/画像/{Agent}/memory/`
   - Anima 专用记忆路径
   - 每个 Agent 独立

**问题：** 两套系统并行，没有同步机制，导致记忆数据分散。

---

## 🏗️ 解决方案：三层同步机制

```
┌─────────────────────────────────────────────────────────┐
│  第一层：实时同步（主流程）                              │
│  - 触发时机：写记忆时立即同步                            │
│  - 位置：anima_tools.py 的 memory_write_v2              │
│  - 延迟：<100ms                                         │
│  - 覆盖率：100%（所有新记忆）                           │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  第二层：启动同步（兜底）                                │
│  - 触发时机：Anima 启动时                                │
│  - 位置：anima-core/core/memory_sync.py                 │
│  - 延迟：<1s                                            │
│  - 覆盖率：100%（补全缺失记忆）                         │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  第三层：定时同步（监控）                                │
│  - 触发时机：手动或 cron 定时                            │
│  - 位置：anima-core/scripts/sync-memory.sh              │
│  - 延迟：<1s                                            │
│  - 覆盖率：100%（可同步所有 Agent）                     │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 使用方法

### 方法 1：实时同步（自动）

**无需手动操作**，写记忆时自动同步：

```python
from anima_tools import memory_write_v2

# 写入记忆（自动同步到画像目录）
result = memory_write_v2(
    content="今天完成了 Anima v5.0.2 开发",
    type="episodic",
    agent_name="枢衡"
)

# 输出：
# ✅ 记忆已同步到画像目录：枢衡/2026-03-21.md
```

---

### 方法 2：启动同步（自动）

**Anima 启动时自动执行**，补全缺失记忆：

```python
from memory_sync import sync_memory_on_startup

# 启动时调用
sync_memory_on_startup("枢衡")

# 输出：
# ✅ 同步记忆：2026-03-10.md
# ✅ 同步记忆：2026-03-13.md
# ...
```

---

### 方法 3：定时同步（手动/自动）

**手动同步：**
```bash
# 同步所有 Agent
/root/.openclaw/workspace-shuheng/projects/anima/anima-core/scripts/sync-memory.sh

# 同步指定 Agent
/root/.openclaw/workspace-shuheng/projects/anima/anima-core/scripts/sync-memory.sh 枢衡
```

**自动同步（可选）：**
```bash
# 添加到 crontab（每小时同步一次）
0 * * * * /root/.openclaw/workspace-shuheng/projects/anima/anima-core/scripts/sync-memory.sh
```

---

## 🏥 Doctor 检查

**检查记忆同步状态：**
```bash
cd /root/.openclaw/workspace-shuheng/projects/anima/anima-skill
python3 anima_doctor.py
```

**输出示例：**
```
诊断结果:
------------------------------------------------------------
✅ skill_installed: Skill 已安装
✅ core_installed: Core 已安装
❌ memory_sync: 记忆未同步到画像目录
✅ dependencies: 依赖正常
------------------------------------------------------------
```

**修复建议：**
```bash
# 运行同步脚本
/root/.openclaw/workspace-shuheng/projects/anima/anima-core/scripts/sync-memory.sh 枢衡

# 或重新写入记忆
# 写记忆时会自动同步
```

---

## 📊 同步策略

| 场景 | 同步方向 | 触发时机 | 延迟 | 覆盖率 |
|------|---------|---------|------|--------|
| 写记忆 | Workspace → 画像 | 立即 | <100ms | 100% |
| 启动时 | Workspace → 画像 | 每次启动 | <1s | 100% |
| 定时同步 | Workspace → 画像 | 手动/cron | <1s | 100% |
| 冲突处理 | 保留最新 | 自动 | - | - |

---

## 🔍 故障排查

### 问题 1：记忆未同步

**症状：**
- Doctor 检查显示 `❌ memory_sync: 记忆未同步到画像目录`

**原因：**
- 实时同步失败（网络/权限问题）
- 启动同步未执行

**解决方案：**
```bash
# 1. 手动同步
/root/.openclaw/workspace-shuheng/projects/anima/anima-core/scripts/sync-memory.sh 枢衡

# 2. 检查权限
chmod -R 755 /home/画像/枢衡/memory

# 3. 重新写入记忆（触发实时同步）
```

---

### 问题 2：同步脚本失败

**症状：**
- 运行 `sync-memory.sh` 报错

**原因：**
- 目录不存在
- 权限不足

**解决方案：**
```bash
# 1. 创建目录
mkdir -p /home/画像/枢衡/memory

# 2. 设置权限
chmod -R 755 /home/画像/枢衡/memory

# 3. 重新运行
/root/.openclaw/workspace-shuheng/projects/anima/anima-core/scripts/sync-memory.sh 枢衡
```

---

### 问题 3：重复同步

**症状：**
- 同一记忆被多次同步

**原因：**
- 实时同步和定时同步同时触发

**解决方案：**
- ✅ 已自动处理（检查文件是否存在）
- ✅ 避免重复写入

---

## 📝 最佳实践

### 1. 写记忆时

```python
# ✅ 推荐：使用 memory_write_v2（自动同步）
memory_write_v2(content="...", agent_name="枢衡")

# ❌ 不推荐：直接写入文件（不同步）
```

### 2. 启动时

```python
# ✅ 推荐：调用 sync_memory_on_startup
sync_memory_on_startup(agent_name)

# ❌ 不推荐：跳过启动同步
```

### 3. 定时同步

```bash
# ✅ 推荐：添加 cron 定时任务
0 * * * * /path/to/sync-memory.sh

# ❌ 不推荐：频繁手动同步
```

---

## 📈 监控指标

| 指标 | 目标值 | 检查方法 |
|------|--------|---------|
| 同步成功率 | >99% | Doctor 检查 |
| 同步延迟 | <100ms | 日志监控 |
| 缺失记忆数 | 0 | sync-memory.sh |
| 重复记忆数 | 0 | 手动检查 |

---

## 🔗 相关文件

| 文件 | 说明 | 路径 |
|------|------|------|
| `anima_tools.py` | 实时同步实现 | `anima-skill/` |
| `memory_sync.py` | 启动同步模块 | `anima-core/core/` |
| `sync-memory.sh` | 定时同步脚本 | `anima-core/scripts/` |
| `anima_doctor.py` | 同步检查 | `anima-skill/` |

---

## 📅 更新历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v5.0.2 | 2026-03-21 | 初始版本，实现三层同步机制 |

---

**维护者：** 枢衡  
**最后审查：** 2026-03-21
