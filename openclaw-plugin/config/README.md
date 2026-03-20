# Anima-AIOS 路径配置

## 🎯 作用

自动检测不同操作系统的路径，支持：
- ✅ Linux 服务器
- ✅ macOS
- ✅ Windows
- ✅ 自定义路径

## 📝 使用方法

### 方式 1：自动检测（推荐）

```python
from config.path_config import get_config

config = get_config()

# 自动获取路径
facts_base = config.facts_base  # /home/画像 (Linux)
openclaw_base = config.openclaw_base  # /root/.openclaw (Linux)
```

### 方式 2：自定义路径

```python
from config.path_config import Config

# macOS 示例
config = Config(
    facts_base='/Users/用户名/画像',
    openclaw_base='/Users/用户名/.openclaw'
)

# Windows 示例
config = Config(
    facts_base='C:/Users/用户名/画像',
    openclaw_base='C:/Users/用户名/.openclaw'
)
```

### 方式 3：环境变量

```bash
# 设置自定义路径
export ANIMA_FACTS_BASE="/custom/path/画像"
export ANIMA_OPENCLAW_BASE="/custom/path/.openclaw"

# Python 中使用
from config.path_config import Config
config = Config(
    facts_base=os.getenv('ANIMA_FACTS_BASE'),
    openclaw_base=os.getenv('ANIMA_OPENCLAW_BASE')
)
```

## 📁 路径说明

### 默认路径（Linux）

| 路径 | 默认值 | 说明 |
|------|--------|------|
| `facts_base` | `/home/画像` | Agent 画像目录 |
| `openclaw_base` | `/root/.openclaw` | OpenClaw 安装目录 |
| `agents_dir` | `/home/画像` | Agent 目录 |
| `backup_dir` | `/home/画像/.backup` | 备份目录 |
| `shared_dir` | `/home/画像/shared` | 共享目录 |
| `message_queue_base` | `/home/消息队列` | 消息队列目录 |
| `openclaw_agents_dir` | `/root/.openclaw/agents` | OpenClaw Agents 目录 |

### macOS 路径

| 路径 | 默认值 |
|------|--------|
| `facts_base` | `/Users/用户名/画像` |
| `openclaw_base` | `/Users/用户名/.openclaw` |

### Windows 路径

| 路径 | 默认值 |
|------|--------|
| `facts_base` | `C:/Users/用户名/画像` |
| `openclaw_base` | `C:/Users/用户名/.openclaw` |

## 🔧 配置文件

### anima_config.json

```json
{
  "paths": {
    "facts_base": "/home/画像",
    "openclaw_base": "/root/.openclaw"
  }
}
```

## 🧪 测试

```bash
# 测试路径配置
cd openclaw-plugin
python3 config/path_config.py
```

**输出示例：**
```
=== 路径配置测试 ===

系统：Linux
facts_base: /home/画像
openclaw_base: /root/.openclaw

完整配置:
  system: Linux
  facts_base: /home/画像
  openclaw_base: /root/.openclaw
  agents_dir: /home/画像
  backup_dir: /home/画像/.backup
  shared_dir: /home/画像/shared
  message_queue_base: /home/消息队列
  openclaw_agents_dir: /root/.openclaw/agents
```

## 📝 最佳实践

1. **使用自动检测** - 大多数情况下无需手动配置
2. **环境变量优先** - 部署时使用环境变量
3. **配置文件备份** - 保存自定义配置
4. **路径验证** - 启动前验证路径存在

## ⚠️ 注意事项

1. **路径存在性** - 确保路径存在或可创建
2. **权限问题** - 确保有读写权限
3. **符号链接** - 支持符号链接
4. **中文路径** - 支持中文路径（UTF-8）

---

**Anima-AIOS v5.0.0** - Making Growth Visible, Making Cognition Measurable
