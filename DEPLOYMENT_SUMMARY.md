# Memora v4.0 Phase 5 & 6 — 部署总结

**部署日期：** 2026-03-20  
**部署范围：** 全部 17 个 Agent  
**状态：** ✅ 已完成

---

## 📊 部署结果

### 已部署 Agent（17 个）

| # | Agent | 目录 | 配置 | 认知画像 | 状态 |
|---|-------|------|------|----------|------|
| 1 | 乐言 | ✅ | ✅ | ✅ | 已完成 |
| 2 | 日安 | ✅ | ✅ | ✅ | 已完成 |
| 3 | 明澈 | ✅ | ✅ | ✅ | 已完成 |
| 4 | 星澜 | ✅ | ✅ | ✅ | 已完成 |
| 5 | 构稳 | ✅ | ✅ | ✅ | 已完成 |
| 6 | 枢衡 | ✅ | ✅ | ✅ | 已完成 |
| 7 | 检严 | ✅ | ✅ | ✅ | 已完成 |
| 8 | 正言 | ✅ | ✅ | ✅ | 已完成 |
| 9 | 流萤 | ✅ | ✅ | ✅ | 已完成 |
| 10 | 游策 | ✅ | ✅ | ✅ | 已完成 |
| 11 | 瑾瑜 | ✅ | ✅ | ✅ | 已完成 |
| 12 | 界安 | ✅ | ✅ | ✅ | 已完成 |
| 13 | 白墨 | ✅ | ✅ | ✅ | 已完成 |
| 14 | 立文 | ✅ | ✅ | ✅ | 已完成 |
| 15 | 糖豆 | ✅ | ✅ | ✅ | 已完成 |
| 16 | 维安 | ✅ | ✅ | ✅ | 已完成 |
| 17 | 青衫 | ✅ | ✅ | ✅ | 已完成 |

### 部署内容

每个 Agent 已配置：
- ✅ `memora_config.json` — 配置文件
- ✅ `facts/episodic/` — episodic facts 目录
- ✅ `facts/semantic/` — semantic facts 目录
- ✅ `daily_quests/` — 每日任务目录
- ✅ `cognitive_profile.json` — 初始认知画像

---

## 🔧 配置说明

### memora_config.json

```json
{
  "version": "4.0.0",
  "agent": "枢衡",
  
  "normalization": {
    "mode": "auto",
    "use_global_benchmark": false,
    "team_size_threshold": {
      "percentile": 5,
      "hybrid": 2,
      "absolute": 1
    }
  },
  
  "weights": {
    "understanding": 0.20,
    "application": 0.20,
    "creation": 0.25,
    "metacognition": 0.15,
    "collaboration": 0.20
  }
}
```

---

## 📋 使用说明

### 1. 查看认知进度

```bash
cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system
./scripts/show-progress.sh 枢衡
```

### 2. 刷新每日任务

```bash
./scripts/refresh-quests.sh 枢衡
```

### 3. 查看任务状态

```bash
cd core
python3 daily_quest.py 枢衡 status
```

### 4. 生成完整画像

```bash
python3 demo.py 枢衡
```

---

## ⏰ Cron 配置（可选）

如需自动任务刷新和检查，手动配置 Cron：

```bash
# 编辑 crontab
crontab -e

# 添加以下任务（替换 AGENT_NAME）
0 5 * * * cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system && ./scripts/refresh-quests.sh 枢衡 >> /var/log/memora-v4/quests_枢衡.log 2>&1
0 * * * * cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system/core && python3 daily_quest.py 枢衡 check >> /var/log/memora-v4/quests_check_枢衡.log 2>&1
0 6 * * * cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system/core && python3 cognitive_profile.py 枢衡 > /var/log/memora-v4/profile_枢衡.log 2>&1
```

---

## 📈 团队扫描

Memora v4.0 会自动扫描活跃 Agent：

```bash
cd core
python3 team_scanner.py
```

**当前检测（2026-03-20 12:05）：**
- 活跃窗口：30 天
- 活跃 Agent：17 个
- 归一化模式：百分位数（大团队）

**归一化模式自动切换：**
- ✅ 当前 17 人 → 百分位数模式
- 如果减少到 2-4 人 → 自动切换到混合模式
- 如果只剩 1 人 → 自动切换到绝对基准

---

## 🎯 试用计划

### 第一周（2026-03-20 ~ 2026-03-27）

**目标：** 熟悉系统，积累初始数据

**任务：**
- [ ] 每日写 1 条 facts（episodic 或 semantic）
- [ ] 每日查看任务状态
- [ ] 周末查看认知画像变化

**预期：**
- 每个 Agent 积累 5-10 条 facts
- 认知分数从 0 提升到 20-40
- 发现并修复潜在问题

---

### 第二周（2026-03-27 ~ 2026-04-03）

**目标：** 开始协作，测试团队功能

**任务：**
- [ ] 写入 shared/ 共享知识
- [ ] 使用 memory_search 检索他人知识
- [ ] 查看团队对比卡片

**预期：**
- 检测到的活跃 Agent ≥3
- 归一化模式切换到混合模式
- 协作认知维度开始有分数

---

### 第三周（2026-04-03 ~ 2026-04-10）

**目标：** 评估效果，收集反馈

**任务：**
- [ ] 收集团队反馈
- [ ] 分析认知成长曲线
- [ ] 调整配置参数

**预期：**
- 确定是否推广到编辑组
- 识别需要改进的功能
- 规划 Phase 7 游戏化

---

## 📞 问题反馈

如遇到问题，请检查：

1. **日志文件**
   ```bash
   tail -f /var/log/memora-v4/quests_枢衡.log
   ```

2. **Python 版本**
   ```bash
   python3 --version  # 需要 3.9+
   ```

3. **目录权限**
   ```bash
   ls -la /home/画像/枢衡/
   ```

4. **重新生成画像**
   ```bash
   cd core
   python3 cognitive_profile.py 枢衡
   ```

---

## 📊 当前状态

**截至 2026-03-20 12:05**

- ✅ 部署完成：17/17 Agent
- ✅ 配置文件：17/17
- ✅ 认知画像：17/17
- ✅ 团队扫描：检测到 17 个活跃 Agent
- ✅ 归一化模式：百分位数（大团队）
- ⏳ 数据积累：等待开始

---

## 🙏 下一步

### 第一阶段：启动（本周）

1. **开始使用** — 每日写 facts，完成任务
2. **查看画像** — 使用 `./scripts/show-progress.sh <Agent 名称>`
3. **团队对比** — 使用 `python3 profile_card.py comparison`

### 第二阶段：观察（2 周后）

1. **收集反馈** — 各 Agent 的使用体验
2. **分析数据** — 认知成长曲线、团队分布
3. **调整参数** — 根据实际数据优化基准值

### 第三阶段：优化（1 个月后）

1. **Phase 7 游戏化** — 成就徽章、排行榜
2. **Phase 8 插件** — OpenClaw 集成
3. **开源准备** — 文档完善、安全脱敏

---

## 🎯 快速命令参考

```bash
# 查看某个 Agent 的认知进度
./scripts/show-progress.sh 枢衡

# 刷新每日任务
./scripts/refresh-quests.sh 枢衡

# 查看任务状态
cd core
python3 daily_quest.py 枢衡 status

# 生成完整画像
python3 demo.py 枢衡

# 查看团队扫描结果
python3 team_scanner.py

# 生成团队对比卡片
python3 profile_card.py 枢衡 comparison
```

---

**Memora v4.0 — 让成长可见，让认知可量化**

部署只是开始，真正的价值在于持续使用和迭代。
