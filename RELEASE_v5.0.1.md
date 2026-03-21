# Anima-AIOS v5.0.1 发布说明

**发布日期：** 2026-03-21  
**版本类型：** Bug 修复版本  
**优先级：** 🔴 推荐升级

---

## 📊 版本信息

| 组件 | 旧版本 | 新版本 | 变更类型 |
|------|--------|--------|----------|
| **anima-skill** | v5.0.0 | v5.0.1 | Bug 修复 |
| **anima-core** | v5.0 | v5.1 | Bug 修复 + 优化 |

---

## 🐛 修复的 Bug

### P0 - 严重 Bug（4 个）

1. **维度名称不一致** - 统一使用 `understanding`
2. **EXP 记录静默失败** - 添加具体异常处理和错误日志
3. **两套等级系统冲突** - 废弃旧方法，统一使用 level_system.py
4. **画像文件不实时更新** - 查询时自动保存

### P1 - 重要 Bug（3 个）

5. **去重检测未实现** - 基于内容哈希检查最近 10 条记忆
6. **质量系数逻辑** - 基础 EXP 和质量奖励分开计算
7. **权重配置未落地** - creation 维度 EXP 提升 20-25%

### P2 - 代码质量（3 个）

8. **静默失败过多** - 修复 4 处 bare except
9. **硬编码 Agent 名称** - 从环境变量获取
10. **路径配置混乱** - 统一为环境变量管理

---

## 🆕 新功能

### anima-skill v5.0.1

- ✅ 错误日志记录（`anima_exp_errors.log`）
- ✅ 去重检测（检查最近 10 条记忆）
- ✅ 环境变量配置（`ANIMA_AGENT_NAME`, `ANIMA_WORKSPACE`, `ANIMA_FACTS_BASE`）

### anima-core v5.1

- ✅ 画像自动更新（查询时自动保存）
- ✅ 质量系数优化（基础 + 奖励分离）
- ✅ 权重配置落地（creation +20-25%）

---

## 📈 改进效果

| 指标 | v5.0.0 | v5.0.1 | 提升 |
|------|--------|--------|------|
| **测试通过率** | - | 12/12 | 100% ✅ |
| **EXP 记录可靠性** | 可能丢失 | 100% | +100% ✅ |
| **维度一致性** | 不一致 | 统一 | 100% ✅ |
| **等级一致性** | 2 套系统 | 统一 | 100% ✅ |
| **画像更新** | 手动 | 自动 | 实时 ✅ |
| **去重检测** | 无 | 有 | +100% ✅ |
| **异常处理** | 7 处 bare | 全部具体 | 100% ✅ |

---

## 🔧 升级步骤

### 方式 1：自动升级（推荐）

```bash
# 停止当前进程
pkill -f "vega-watcher"

# 重新安装
cd /root/.openclaw/workspace-shuheng/projects/anima
bash install.sh

# 重启 Vega
nohup vega-watcher 你的 Agent 名称 > /dev/null 2>&1 &
```

### 方式 2：Git 升级

```bash
cd /root/.openclaw/workspace-shuheng/projects/anima
git pull origin main

# 重启服务
pkill -f "vega-watcher"
nohup vega-watcher 你的 Agent 名称 > /dev/null 2>&1 &
```

---

## ✅ 验证升级

```bash
# 1. 检查版本
cd /root/.openclaw/workspace-shuheng/projects/anima
git log -1 --oneline

# 2. 运行测试
cd anima-skill
python3 test-integration.py

# 3. 验证功能
python3 -c "from anima_tools import get_cognitive_profile; print(get_cognitive_profile('你的 Agent 名称'))"
```

**预期输出：**
```
✅ 测试通过：12/12 (100%)
✅ EXP 记录正常
✅ 等级计算正确
✅ 画像文件实时更新
```

---

## 📝 已知问题

无

---

## 📚 相关文档

- [BUG_FIX_REPORT_20260321.md](docs/BUG_FIX_REPORT_20260321.md) - 完整 Bug 修复报告
- [CHANGELOG.md](CHANGELOG.md) - 变更日志
- [USAGE.md](anima-skill/USAGE.md) - 使用手册
- [ARCHITECTURE_PRINCIPLES.md](docs/ARCHITECTURE_PRINCIPLES.md) - 架构原则

---

## 🙏 致谢

- **立文** - 战略指导
- **日安** - Bug 报告、测试支持

---

## 📄 许可证

MIT License

---

**Anima-AIOS — Making Growth Visible, Making Cognition Measurable**

**让成长可见，让认知可量**

---

**GitHub:** https://github.com/anima-aios/anima  
**版本：** v5.0.1 (skill) / v5.1 (core)  
**发布日期：** 2026-03-21
