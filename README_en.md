# 🌟 Anima-AIOS

> **Making Growth Visible, Making Cognition Measurable**

[![Version](https://img.shields.io/badge/version-6.0.0-green.svg)](https://github.com/anima-aios/anima/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-OpenClaw-purple.svg)](https://openclaw.ai)

Add **5-layer memory architecture, Knowledge Palace, cognitive growth, and auto-evolution** to your AI Agent. Track every learning moment, quantify every progress.

---

## ✨ Core Features

### 🏗️ 5-Layer Memory Architecture

```
Agent daily work (OpenClaw write/edit/memory_write)
       │
       ▼  watchdog listener, zero-intrusion
 L1 Working Memory ── workspace/memory/*.md
       │ Sink
       ▼
 L2 Episodic Memory ── facts/episodic/ (LLM quality assessment)
       │ Distill
       ▼
 L3 Semantic Memory ── facts/semantic/ (LLM dedup + association)
       │ Structure
       ▼
 L4 Knowledge Palace ── palace/rooms/ (LLM classify + debounce)
    Pyramid         ── pyramid/ (instances→rules→patterns→ontology)
       │ Reflect
       ▼
 L5 Meta-Cognition ── 5D profile + EXP + decay + health
```

### 🏛️ Knowledge Palace
- Palace → Floor → Room → Locus → Item, 5-level spatial structure
- LLM-powered classification + deferred debounce scheduler
- Default 4 rooms + _inbox fallback

### 🔺 Pyramid Knowledge Organization
- Instances → Rules → Patterns → Ontology, bottom-up distillation
- Auto-distill when ≥ 3 instances on the same topic

### 📉 Memory Decay Function
- Based on Ebbinghaus forgetting curve + AI adaptation
- Review = Access: each search hit refreshes strength
- Review recommendations + forgetting alerts

### 🔌 Native OpenClaw Integration
- Based on `watchdog` library, auto-detects inotify/FSEvents/WinAPI
- Agent writes memory → Anima syncs automatically, zero friction

### 🤖 LLM-Powered Processing
- Quality assessment / dedup / palace classification all support LLM
- Multi-model config: default uses current Agent model, configurable per task
- Auto-fallback to rule-based when LLM unavailable

### 📊 5-Dimensional Cognitive Profile
- **Internalization** · **Application** · **Creation** · **Metacognition** · **Collaboration**
- Fair normalization algorithm, comparable across Agents

### 🎮 Gamified Growth
- **Level System**: Lv.1 ~ Lv.100
- **Daily Quests**: 3 challenges per day
- **Team Leaderboard**: EXP ranking + real-time competition

### 🏥 Health System (5 modules)
- Hygiene · Correction · Evolution · Abstraction · Manager

---

## 🚀 Quick Start

### Install

```bash
# Via ClawHub
clawhub install anima-aios

# Or manual install
git clone https://github.com/anima-aios/anima.git
cp -r anima/anima-aios ~/.openclaw/skills/anima-aios
```

### Dependencies

```bash
pip install watchdog
```

### Usage

After installation, Anima works automatically:
- Write memory → auto-sync to L2 + earn EXP
- Search memory → auto-refresh decay strength
- Daily 3:00 AM → auto distill + palace classify + pyramid distill

---

## 📁 Project Structure

```
anima-aios/
├── core/                 # Core modules (18)
│   ├── memory_watcher.py     # L1→L2 file watcher
│   ├── fact_store.py         # L2/L3 fact storage
│   ├── distill_engine.py     # L2→L3 LLM distillation
│   ├── palace_index.py       # L4 palace index
│   ├── pyramid_engine.py     # L4 pyramid knowledge org
│   ├── palace_classifier.py  # L4 classifier (debounce)
│   ├── decay_function.py     # L5 memory decay
│   ├── cognitive_profile.py  # 5D cognitive profile
│   ├── exp_tracker.py        # EXP tracking
│   └── ...
├── health/               # Health system (5 modules)
├── tests/                # Tests (unit + integration)
├── scripts/              # Utility scripts
├── config/               # Configuration
├── docs/                 # Documentation
└── assets/               # Screenshots
```

---

## 🧪 Testing

```bash
# Run v6 integration tests (37 checks)
cd anima-aios && python3 tests/test_integration_v6.py
```

---

## 📄 License

[Apache License 2.0](LICENSE)

---

_Architecture can only evolve, never regress._
_Be honest first, then iterate. Code must live up to its promises._

**Version:** v6.0.0 | **Last Updated:** 2026-03-24
