# 🛰️ Blacky Orbit

**Personal Agentic Workspace — Multi-Agent System for Web3 Opportunity Intelligence + Autonomous Code Generation**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![MiMo](https://img.shields.io/badge/Powered%20by-Xiaomi%20MiMo%20V2.5-orange.svg)](https://platform.xiaomimimo.com)
[![Hermes](https://img.shields.io/badge/Framework-Hermes%20Agent-purple.svg)](https://hermes-agent.nousresearch.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agents](https://img.shields.io/badge/Agents-8%20Active-brightgreen.svg)](#agent-fleet)

> **~16B tokens/day** consumed across 8 specialized AI agents — orchestrating Web3 opportunity discovery, eligibility analysis, and autonomous code generation 24/7.

Blacky Orbit is a personal agentic workspace built on top of [Hermes Agent](https://hermes-agent.nousresearch.com) framework. It combines two real-world workflows that consume heavy token budgets: **Web3 opportunity intelligence** (airdrop discovery, eligibility scoring, anti-sybil hygiene) and **autonomous code generation** (multi-pass refactor, security review, TDD loops).

The orchestration layer leverages MiMo-V2.5-Pro's long-chain reasoning for high-stakes decisions and MiMo-V2.5 for high-frequency analysis tasks.

---

## 🏗️ Architecture

```
                       ┌─────────────────────────┐
                       │   🧠 Orchestrator        │
                       │   (MiMo-V2.5-Pro)       │
                       │   Task Routing &         │
                       │   Decision Hub           │
                       └────────────┬─────────────┘
                                    │
        ┌────────────┬──────────────┼──────────────┬────────────┐
        │            │              │              │            │
   ┌────▼────┐  ┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐  ┌────▼────┐
   │ Hunter  │  │Eligibility│ │ Guardian │  │  Chain   │  │  Coder  │
   │ Agent   │  │  Agent    │ │  Agent   │  │  Agent   │  │  Agent  │
   │ Web3    │  │ Wallet    │ │ Anti-    │  │  TX Sim  │  │  Code   │
   │ Scout   │  │ Analysis  │ │ Sybil    │  │  + Verify│  │  Gen    │
   └─────────┘  └───────────┘ └──────────┘  └──────────┘  └─────────┘
                                    │
                       ┌────────────┼─────────────┐
                       │                          │
                  ┌────▼─────┐              ┌────▼─────┐
                  │ Reviewer │              │  Scribe  │
                  │  Agent   │              │  Agent   │
                  │ Security │              │  Docs &  │
                  │  Audit   │              │ Tracking │
                  └──────────┘              └──────────┘
```

---

## 🤖 Agent Fleet

| Agent | Model | Role | Tokens/Day |
|-------|-------|------|-----------:|
| 🧠 Orchestrator | MiMo-V2.5-Pro | Task routing, multi-agent coordination, decision making | 2.5B |
| 🔍 Hunter | MiMo-V2.5-Pro | Continuous airdrop / quest / testnet opportunity discovery | 2.0B |
| 📊 Eligibility | MiMo-V2.5-Pro | Per-wallet deep eligibility scoring across 100+ projects | 1.5B |
| 🛡️ Guardian | MiMo-V2.5-Pro | 4-pass anti-sybil pattern detection + scam contract analysis | 1.8B |
| 🔗 Chain | MiMo-V2.5 | On-chain TX simulation, slippage check, gas optimization | 2.2B |
| 💻 Coder | MiMo-V2.5-Pro | Autonomous code generation, refactor, TDD iteration loops | 3.0B |
| 🔬 Reviewer | MiMo-V2.5 | Security audit, style check, dependency vulnerability scan | 2.0B |
| 📝 Scribe | MiMo-V2.5 | Documentation, daily summaries, audit logs, knowledge base | 1.0B |

**Total: ~16B tokens/day | ~480B tokens/month**

---

## 🔬 4-Pass Reasoning Pipelines

### Anti-Sybil Detection (Guardian Agent)

```
Pass 1 — Wallet Fingerprint
  └─ TX history pattern, gas usage, token interaction graph

Pass 2 — Cluster Analysis  
  └─ Cross-wallet behavior correlation, IP/timing collisions

Pass 3 — Counter-Heuristic
  └─ Test pattern against known sybil-detection algorithms
     used by major projects (LayerZero, zkSync, Linea, etc.)

Pass 4 — MiMo-V2.5-Pro Synthesis
  └─ Long-chain reasoning produces final risk score
     + actionable hygiene recommendations
```

### Code Generation (Coder Agent)

```
Pass 1 — Spec Decomposition
  └─ Break high-level intent into testable units

Pass 2 — TDD Skeleton
  └─ Write failing tests first, define contracts

Pass 3 — Implementation
  └─ Generate code, run tests, iterate until green

Pass 4 — Refactor + Reviewer Handoff
  └─ Pass to Reviewer Agent for security + style audit
```

---

## 📊 Operational Metrics (Target)

- **15+** active airdrop projects monitored simultaneously
- **8+** EVM chains tracked (Ethereum, Base, Arbitrum, Optimism, Linea, zkSync, Scroll, Polygon)
- **24/7** continuous opportunity discovery
- **<5min** average eligibility assessment per wallet
- **<30min** end-to-end code generation pipeline (spec → tested PR)
- **~16B** tokens consumed daily across all agents

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker & docker-compose (optional, for full stack)
- MiMo API credentials from [platform.xiaomimimo.com](https://platform.xiaomimimo.com)
- Hermes Agent installed ([install guide](https://hermes-agent.nousresearch.com/docs))

### Installation

```bash
# Clone
git clone https://github.com/OxNolan/blacky-orbit.git
cd blacky-orbit

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your MiMo API key + Hermes config

# Run orchestrator
python -m src.main --config config/default.yaml
```

### Docker

```bash
docker-compose up -d
docker-compose logs -f orchestrator
```

---

## ⚙️ Configuration

Sample `config/default.yaml`:

```yaml
mimo:
  api_url: https://api.xiaomimimo.com/v1
  model_primary: mimo-v2.5-pro
  model_secondary: mimo-v2.5
  max_tokens_per_request: 32000
  rate_limit_rps: 50

hermes:
  framework: hermes-agent
  delegation_max_depth: 2
  memory_backend: sqlite

agents:
  orchestrator:
    enabled: true
    model: mimo-v2.5-pro
    concurrency: 8

  hunter:
    enabled: true
    model: mimo-v2.5-pro
    sources: [galxe, layer3, zealy, defillama, x_alpha_feeds]
    poll_interval: 5m

  eligibility:
    enabled: true
    model: mimo-v2.5-pro
    chains: [ethereum, base, arbitrum, optimism, linea, zksync, scroll, polygon]

  guardian:
    enabled: true
    model: mimo-v2.5-pro
    passes: 4
    min_confidence: 0.85

  chain:
    enabled: true
    model: mimo-v2.5
    simulate_before_send: true

  coder:
    enabled: true
    model: mimo-v2.5-pro
    tdd_iterations: 5
    refactor_passes: 2

  reviewer:
    enabled: true
    model: mimo-v2.5
    security_rules: owasp-2025

  scribe:
    enabled: true
    model: mimo-v2.5
    output: obsidian
```

---

## 🛠️ Tech Stack

- **AI Models:** MiMo-V2.5-Pro (reasoning), MiMo-V2.5 (analysis)
- **Agent Framework:** [Hermes Agent](https://hermes-agent.nousresearch.com)
- **Editor Integrations:** Cursor, Claude Code, Hermes CLI
- **Blockchain Data:** Etherscan, Basescan, Arbiscan, Blockscout, Dune, DefiLlama
- **Storage:** SQLite (local), Obsidian (knowledge base), Redis (agent message bus)
- **Deploy:** Docker Compose (local), VPS-ready

---

## 📂 Repository Structure

```
blacky-orbit/
├── src/
│   ├── main.py                  # Entry point + orchestrator boot
│   ├── orchestrator.py          # Task routing & decision hub
│   ├── agents/
│   │   ├── hunter.py            # Web3 opportunity discovery
│   │   ├── eligibility.py       # Wallet eligibility analysis
│   │   ├── guardian.py          # Anti-sybil + scam detection
│   │   ├── chain.py             # On-chain TX simulation
│   │   ├── coder.py             # Code generation
│   │   ├── reviewer.py          # Security + style review
│   │   └── scribe.py            # Docs + tracking
│   ├── mimo_client.py           # MiMo API wrapper
│   └── utils/
├── config/
│   └── default.yaml             # Agent + model config
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🔒 Security & Privacy

- All credentials stored in `.env` (gitignored) or `~/.agent/credentials/`
- Per-transaction confirmation required for any on-chain action involving real funds
- Wallet addresses are read-only by default; signing operations require explicit user approval
- API keys never logged in plaintext

---

## 📈 Roadmap

- [x] 8-agent multi-agent skeleton
- [x] MiMo-V2.5 integration
- [x] Hermes Agent framework integration
- [ ] Full Hunter agent with 5+ source feeds
- [ ] Guardian 4-pass anti-sybil pipeline
- [ ] Web UI dashboard (Next.js)
- [ ] Per-agent telemetry + cost analytics
- [ ] Integration with Obsidian for knowledge persistence
- [ ] CLI plugin for Cursor + Claude Code

---

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

**Powered by [Xiaomi MiMo V2.5](https://platform.xiaomimimo.com)** — long-chain reasoning that makes 24/7 autonomous multi-agent workflows possible.

**Built on [Hermes Agent](https://hermes-agent.nousresearch.com)** — open-source agent framework for orchestrating LLM-driven workflows.
