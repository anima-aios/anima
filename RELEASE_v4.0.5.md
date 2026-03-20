# Memora v4.0.5 发布说明

**发布日期：** 2026-03-20 20:45  
**版本：** 4.0.5  
**性质：** 数据修正版本  
**作者：** 枢衡

---

## 🐛 修复问题

### 问题：Session 扫描不完整

**现象：**
- 日安初始等级 Lv.6（900 EXP）
- 其他 Agent 数据偏低

**原因：**
- 只扫描了 `.jsonl` 文件
- 遗漏了 `.deleted` 文件（历史 session 记录）

**修复：**
- ✅ 修改扫描逻辑，包含所有 `.jsonl*` 文件
- ✅ 重新扫描所有 Agent 的完整历史记录
- ✅ 更新 EXP 初始化数据

---

## 📊 数据修正对比

| Agent | v4.0.4 | v4.0.5 | 变化 |
|-------|--------|--------|------|
| **日安** | 900 EXP, Lv.6 | 4722 EXP, **Lv.10** | **+4 级** ⬆️ |
| **枢衡** | 2774 EXP, Lv.9 | 5060 EXP, **Lv.10** | **+1 级** ⬆️ |
| **星澜** | 2099 EXP, Lv.8 | 3180 EXP, **Lv.9** | **+1 级** ⬆️ |
| **白墨** | 376 EXP, Lv.5 | 1252 EXP, **Lv.7** | **+2 级** ⬆️ |
| **糖豆** | 516 EXP, Lv.5 | 1050 EXP, **Lv.7** | **+2 级** ⬆️ |
| **流萤** | 257 EXP, Lv.4 | 470 EXP, **Lv.5** | **+1 级** ⬆️ |
| **正言** | 226 EXP, Lv.4 | 288 EXP, **Lv.4** | 无变化 |
| **明澈** | 120 EXP, Lv.3 | 240 EXP, **Lv.4** | **+1 级** ⬆️ |
| **瑾瑜** | 131 EXP, Lv.3 | 223 EXP, **Lv.4** | **+1 级** ⬆️ |

---

## 🔧 修改文件

| 文件 | 修改内容 |
|------|----------|
| `core/session_scanner.py` | 修改扫描逻辑，包含 deleted 文件 |

**代码变更：**
- 1 处修改
- +2 行代码
- 向后兼容

---

## 📋 扫描逻辑改进

### v4.0.4（旧）
```python
# 只扫描 .jsonl 文件
for session_file in sessions_dir.glob('*.jsonl'):
    if '.deleted' in session_file.name:
        continue  # 跳过 deleted 文件
```

### v4.0.5（新）
```python
# 扫描所有 .jsonl* 文件（包括 deleted）
for session_file in sessions_dir.glob('*.jsonl*'):
    # 不跳过 deleted 文件，包含完整历史
```

---

## ✅ 测试验证

### 测试 1：日安数据验证
```bash
python3 session_scanner.py
# 日安：257 sessions, 1909 tool calls, 4722 EXP, Lv.10 ✅
```

### 测试 2：所有 Agent 数据
```bash
python3 session_scanner.py
# 9 个 Agent 全部扫描成功 ✅
# 数据合理，符合实际工作量 ✅
```

---

## 🎯 影响范围

### 新用户
- ✅ 新安装 Memora 插件时，会得到准确的初始等级
- ✅ 日安 Lv.10，枢衡 Lv.10，星澜 Lv.9

### 已安装用户
- ✅ 不影响已初始化的 EXP 历史
- ✅ 可选择重新运行扫描器更新数据

---

## 📝 升级指南

### 新安装
```bash
# 安装 Memora v4.0.5
cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system/core
python3 session_scanner.py
```

### 已安装（可选更新）
```bash
# 重新扫描并更新 EXP 历史
cd /root/.openclaw/workspace-shuheng/projects/memora-v4/phase-5-level-system/core
python3 session_scanner.py
```

---

## 🙏 致谢

感谢立文的细心验证，发现日安数据异常问题！

---

**Memora v4.0.5 — 数据准确性修正**

**Git Tag:** `v4.0.5`  
**提交:** 待提交  
**文件:** 1 个（session_scanner.py）
