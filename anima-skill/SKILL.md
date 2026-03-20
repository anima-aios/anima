# Anima-AIOS Skill

Anima-AIOS 个人智能操作系统 - OpenClaw Skill 插件

## 功能

- 记忆管理（Memora）
- 经验值追踪（EXP Tracker）
- 每日任务系统（Daily Quest）
- 认知评分标准化（Normalization Engine）

## 安装

```bash
# 自动安装（推荐）
curl -fsSL https://raw.githubusercontent.com/anima-aios/anima/main/install.sh | bash

# 或手动安装
cd ~/.openclaw/workspace-shuheng/skills/
ln -s ../../projects/anima/anima-skill anima
```

## 配置

在 `~/.openclaw/config.json` 中添加：

```json
{
  "skills": {
    "anima": {
      "enabled": true,
      "config_path": "~/.anima/anima_config.json"
    }
  }
}
```

## 使用示例

### 添加记忆

```
记住：今天完成了 Vega 消息系统 v2.0.1 的架构重构
```

### 查询经验值

```
我的经验值是多少？
```

### 查看每日任务

```
今天的任务是什么？
```

## 版本

v5.0.0

## 许可证

MIT
