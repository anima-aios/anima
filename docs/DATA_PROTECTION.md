# Memora v4.0 - 数据保护规范

**版本：** 1.0  
**创建日期：** 2026-03-20  
**状态：** ✅ 强制执行

---

## ⚠️ 问题背景

2026-03-20 清理测试数据时，误删了所有 Agent 的：
- facts/ 目录（认知事实数据）
- cognitive_profile.json（认知画像）
- exp_history.jsonl（EXP 历史记录）

**影响：** 所有 Memora 数据丢失，需要重新积累

**教训：** 必须建立严格的数据保护机制

---

## 🛡️ 数据保护措施

### 1. 保护标记文件

**位置：** `/home/画像/{Agent}/DO_NOT_DELETE.txt`

**内容：**
```
# ⚠️ 重要数据目录

此目录包含 Memora v4.0 的重要数据：
- facts/ - 认知事实数据
- cognitive_profile.json - 认知画像
- exp_history.jsonl - EXP 历史记录

⚠️ 删除前请确认：
1. 已备份数据
2. 已获得枢衡授权
3. 确认真的需要删除

备份位置：/home/画像/.backup
```

**作用：** 提醒操作者这是重要数据，不要误删

---

### 2. 自动备份脚本

**脚本：** `scripts/protect-data.sh`

**功能：**
- ✅ 备份所有 Agent 的 facts 数据
- ✅ 备份所有 Agent 的认知画像
- ✅ 创建带时间戳的备份
- ✅ 创建保护标记文件

**用法：**
```bash
cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system
bash scripts/protect-data.sh
```

**备份位置：** `/home/画像/.backup/`

---

### 3. 清理前检查脚本

**脚本：** `scripts/safe-cleanup-check.sh`

**功能：**
- ✅ 检查是否是 Memora 数据目录
- ✅ 检查保护标记
- ✅ 检查是否有备份
- ✅ 统计待删除数据
- ✅ 多次确认删除

**用法：**
```bash
# 删除前必须运行
./scripts/safe-cleanup-check.sh /home/画像/枢衡/facts
```

**保护机制：**
1. 检测到保护标记 → 显示警告
2. 没有备份 → 建议先备份
3. 需要输入"YES"确认
4. 需要输入"DELETE"最终确认

---

### 4. 定期备份（Cron）

**配置：** `cron/memora-backup-crontab`

**备份频率：**
- **每日备份：** 每天凌晨 03:00
- **每周清理：** 每周日凌晨 04:00（清理 30 天前的备份）

**安装：**
```bash
cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system
crontab cron/memora-backup-crontab
```

---

## 📋 数据删除流程

### 标准流程

**步骤 1：备份数据**
```bash
./scripts/protect-data.sh
```

**步骤 2：运行检查**
```bash
./scripts/safe-cleanup-check.sh <要删除的目录>
```

**步骤 3：获得授权**
- 联系枢衡说明删除原因
- 获得枢衡书面授权（Vega 消息或飞书）

**步骤 4：执行删除**
```bash
# 检查脚本会提示手动执行
rm -rf <目录>
```

**步骤 5：验证删除**
```bash
ls <目录>  # 应该不存在
```

**步骤 6：记录删除**
- 在删除日志中记录
- 通知相关 Agent

---

## ⚠️ 禁止行为

### ❌ 绝对禁止

1. **直接 rm -rf 整个 Agent 目录**
   ```bash
   # ❌ 禁止
   rm -rf /home/画像/枢衡/
   
   # ✅ 正确
   ./scripts/safe-cleanup-check.sh /home/画像/枢衡/facts
   ```

2. **不备份直接删除**
   ```bash
   # ❌ 禁止
   rm -rf /home/画像/枢衡/facts/
   
   # ✅ 正确
   ./scripts/protect-data.sh
   ./scripts/safe-cleanup-check.sh /home/画像/枢衡/facts
   ```

3. **删除保护标记文件**
   ```bash
   # ❌ 禁止
   rm /home/画像/枢衡/DO_NOT_DELETE.txt
   ```

4. **未经授权使用他人目录**
   ```bash
   # ❌ 禁止
   rm -rf /home/画像/明澈/facts/  # 未获得明澈授权
   ```

---

## 📊 备份管理

### 备份位置

```
/home/画像/.backup/
├── facts/
│   ├── 枢衡_20260320_190604/
│   ├── 明澈_20260320_190604/
│   └── ...
└── profiles/
    ├── 枢衡_20260320_190604.json
    ├── 明澈_20260320_190604.json
    └── ...
```

### 备份保留策略

| 备份类型 | 保留时间 | 清理频率 |
|----------|----------|----------|
| **每日备份** | 30 天 | 每周清理 |
| **手动备份** | 永久 | 不清理 |
| **特殊备份** | 永久 | 不清理 |

### 恢复数据

**从备份恢复：**
```bash
# 恢复 facts 数据
cp -r /home/画像/.backup/facts/枢衡_20260320_190604/ /home/画像/枢衡/facts/

# 恢复认知画像
cp /home/画像/.backup/profiles/枢衡_20260320_190604.json /home/画像/枢衡/cognitive_profile.json
```

---

## 📝 责任分工

| 角色 | 职责 | 权限 |
|------|------|------|
| **枢衡** | 数据保护负责人 | 批准删除、恢复数据 |
| **日安** | 监督 | 审核删除申请 |
| **各 Agent** | 自我保护 | 查看自己的数据 |

---

## 🚨 违规处理

| 违规级别 | 行为 | 处理 |
|----------|------|------|
| **一级** | 未备份删除 | Vega 警告 + 恢复数据 |
| **二级** | 绕过检查删除 | 飞书通报 + 限制权限 |
| **三级** | 恶意删除 | 上报立文 + 严肃处理 |

---

## 📞 紧急联系

**数据丢失紧急处理：**

1. **立即停止操作** - 防止进一步损坏
2. **联系枢衡** - Vega 消息或飞书
3. **从备份恢复** - `/home/画像/.backup/`
4. **记录事件** - 写入事件日志

---

**数据保护，人人有责！**

**版本：** 1.0  
**最后更新：** 2026-03-20 19:06
