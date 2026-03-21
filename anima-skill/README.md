# Anima-AIOS Skill - 自动安装说明

## 📦 安装流程

### 通过 ClawHub 安装（推荐）

```bash
clawhub install anima
```

安装过程：

```
🚀 ════════════════════════════════════════════
🚀       正在安装 Anima-AIOS 认知操作系统
🚀 ════════════════════════════════════════════

[1/5] 检查 Python 环境...
✅ Python 3.9.25 已安装

[2/5] 检查 Git...
✅ Git 2.39.5 已安装

[3/5] 检查 Anima-AIOS core...
📦 未检测到 core，正在安装...
   → 克隆仓库...
   → 执行安装脚本...
✅ Anima-AIOS core 安装完成

[4/5] 安装 Python 依赖...
✅ Python 依赖安装完成

[5/5] 验证安装...
✅ 核心文件验证通过

🎉 ════════════════════════════════════════════
🎉          Anima-AIOS 安装完成！
🎉 ════════════════════════════════════════════

✨ 现在可以使用以下功能：

   📊 认知画像
      '我的认知画像是什么？'

   📈 经验值查询
      '我的经验值是多少？'
      '我现在的等级是多少？'

   🎮 每日任务
      '今天的任务是什么？'
      '完成任务：写周报'

   🔍 智能记忆
      '搜索关于 Vega 的记忆'
      '记住：今天完成了 Anima v5.0 发布'

   📊 团队排行
      '查看团队 EXP 排行榜'

📚 更多文档：https://github.com/anima-aios/anima
```

---

## 🔧 手动安装

如果自动安装失败，可以手动安装：

### 步骤 1：安装 core

```bash
git clone --depth 1 https://github.com/anima-aios/anima.git /tmp/anima
bash /tmp/anima/install.sh
rm -rf /tmp/anima
```

### 步骤 2：验证 core 安装

```bash
ls -la ~/.anima/
# 应该看到：
# - core/
# - config/
# - scripts/
# - anima_config.json
```

### 步骤 3：安装 skill

```bash
cd ~/.openclaw/workspace-shuheng/skills/
ln -s ../../projects/anima/anima-skill anima
```

### 步骤 4：启用 skill

在 `~/.openclaw/config.json` 中添加：

```json
{
  "skills": {
    "anima": {
      "enabled": true
    }
  }
}
```

---

## ❓ 故障排查

### 问题 1：Python 版本过低

```
❌ 错误：需要 Python 3
请安装 Python 3.8+ 后重试
```

**解决：**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# macOS
brew install python3

# CentOS/RHEL
sudo yum install python3 python3-pip
```

### 问题 2：Git 未安装

```
❌ 错误：需要 Git
请安装 Git 后重试
```

**解决：**
```bash
# Ubuntu/Debian
sudo apt install git

# macOS
brew install git

# CentOS/RHEL
sudo yum install git
```

### 问题 3：网络问题（克隆失败）

```
fatal: unable to access 'https://github.com/anima-aios/anima.git': ...
```

**解决：**
```bash
# 检查网络连接
ping github.com

# 使用镜像（中国大陆）
git clone https://github.com.cnpmjs.org/anima-aios/anima.git /tmp/anima

# 或手动下载 ZIP 解压
wget https://github.com/anima-aios/anima/archive/main.zip
unzip main.zip
cd anima-main
bash install.sh
```

### 问题 4：权限问题

```
Permission denied: ~/.anima
```

**解决：**
```bash
# 检查目录权限
ls -la ~/.anima

# 修复权限
chmod -R 755 ~/.anima
chown -R $USER:$USER ~/.anima
```

### 问题 5：skill 未加载

**检查：**
```bash
# 确认 skill 文件存在
ls -la ~/.openclaw/workspace-shuheng/skills/anima/

# 确认 _meta.json 格式正确
cat ~/.openclaw/workspace-shuheng/skills/anima/_meta.json | python3 -m json.tool

# 重启 OpenClaw Gateway
openclaw gateway restart
```

---

## 📊 验证安装

安装完成后，运行以下命令验证：

```bash
# 1. 检查 core 目录
ls ~/.anima/core/
# 应该看到：exp_tracker.py, cognitive_profile.py, daily_quest.py 等

# 2. 检查 skill 目录
ls ~/.openclaw/workspace-shuheng/skills/anima/
# 应该看到：SKILL.md, _meta.json, post-install.sh

# 3. 测试 Python 导入
python3 -c "import sys; sys.path.insert(0, '$HOME/.anima/core'); import exp_tracker; print('✅ core 导入成功')"

# 4. 在 OpenClaw 中测试
# 发送消息："我的经验值是多少？"
```

---

## 🔄 更新

### 自动更新（推荐）

```bash
clawhub update anima
```

### 手动更新

```bash
# 更新 core
cd ~/.anima
git pull origin main
bash install.sh

# 更新 skill
cd ~/.openclaw/workspace-shuheng/skills/anima
git pull origin main

# 重启 OpenClaw
openclaw gateway restart
```

---

## 📚 更多文档

- [主文档](../README.md)
- [部署指南](../DEPLOYMENT_SUMMARY.md)
- [变更日志](../CHANGELOG.md)
- [GitHub](https://github.com/anima-aios/anima)

---

**版本：** v5.0.0  
**最后更新：** 2026-03-21
