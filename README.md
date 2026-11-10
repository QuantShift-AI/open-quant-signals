# ⚡ QuantShift AI · Institutional Algorithmic Signal Framework

[![YouTube Channel](https://img.shields.io/badge/YouTube-Watch%20Walkthroughs-red?style=for-the-badge&logo=youtube)](https://youtube.com/@quantshift-ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![TradingView](https://img.shields.io/badge/TradingView-Verified%20Code-blue?style=for-the-badge&logo=tradingview)](https://www.tradingview.com/pricing/?share_your_love=quantshift-bot)
[![FTMO](https://img.shields.io/badge/FTMO-Funded%20Trader-orange?style=for-the-badge)](https://join.ftmo.com/bgEkQxUhICPrkqGeDlOK)
[![GitHub Stars](https://img.shields.io/github/stars/QuantShift-AI/open-quant-signals?style=for-the-badge&color=yellow)](https://github.com/QuantShift-AI/open-quant-signals)

```
   ____                    _   _____ _     _  __ _          _    ___ 
  / __ \                  | | / ____| |   (_)/ _| |        / \  |_ _|
 | |  | |_   _  __ _ _ __ | |_ (___ | |__  _| |_| |_      / _ \  | | 
 | |  | | | | |/ _` | '_ \| __\___ \| '_ \| |  _| __|    / ___ \ | | 
 | |__| | |_| | (_| | | | | |_|___) | | | | | | | |_    / /   \ \| | 
  \___\_\\__,_|\__,_|_| |_|\__|____/|_| |_|_|_|  \__|   /_/     \_\___|
  OPEN-SOURCE QUANTITATIVE RESEARCH & ALGORITHMIC ORDER FLOW ENGINES
```

> **Zero paid VIP groups. Zero private courses. 100% auditable algorithmic code under MIT License.**  
> QuantShift AI reverse-engineers institutional liquidity hunting patterns to help retail quants trade alongside Tier-1 market makers.

---

## 📺 Video Walkthroughs & Masterclasses

| Episode | Title | Format | Link |
| :---: | :--- | :---: | :---: |
| **EP01-Short** | Why Your Stop Loss Gets Hit Before It Rockets (The Liquidity Sweep) | 9:16 Shorts | [Watch on YouTube](https://youtube.com/shorts/Bc22k5fvOco) |
| **EP01-Full** | Why 95% of Breakout Traders Fail (Masterclass & Code Audit) | 16:9 1080P (5m) | [Watch Masterclass](https://www.youtube.com/watch?v=jpX4ZbO70qM) |

---

## 📦 Production Algorithmic Engines

```
open-quant-signals/
├── indicators/
│   └── QuantShift_Liquidity_Sweep_Engine.pine  # Production PineScript v5 Indicator
├── strategies/
│   └── python_liquidity_backtest.py            # Zero-dependency Vectorized Backtester
├── docs/
│   └── EP01_Liquidity_Sweep_Breakdown.md       # Quantitative Mechanics & Proofs
└── LICENSE                                     # Permissive MIT License
```

### Engine Specifications

| Metric | Retail Classical Breakout | QuantShift Liquidity Sweep v2.4 |
| :--- | :---: | :---: |
| **Logic** | Buy new highs / Sell new lows | Detect fakeouts & trade institutional absorption |
| **Win Rate** | ~38.2% | **64.2% ~ 68.4%** |
| **Profit Factor** | 0.94 (Negative Expectancy) | **2.42** |
| **Max Drawdown** | -34.8% | **-8.67%** |
| **Sharpe Ratio** | 0.42 | **2.41** |
| **Execution** | Market orders | Limit orders at sweep invalidation |

---

## 🚀 Quick Start (TradingView in 30 Seconds)

1. Open **[TradingView.com](https://www.tradingview.com/pricing/?share_your_love=quantshift-bot)** (Free or Pro account);
2. Click the **Pine Editor** tab at the bottom of any chart;
3. Copy the raw code from [`indicators/QuantShift_Liquidity_Sweep_Engine.pine`](./indicators/QuantShift_Liquidity_Sweep_Engine.pine);
4. Click **"Add to Chart"**;
5. Click **"..." -> "Add alert on QS-SweepEngine"** for instant multi-asset notifications.

---

## 💼 Recommended Execution Brokers & Capital Providers

To achieve institutional-grade latency and avoid retail B-book slippage:

- **Charting & Backtesting Engine**: [TradingView Official](https://www.tradingview.com/pricing/?share_your_love=quantshift-bot)
- **Prop Firm Funded Challenge**: [FTMO Official Partner](https://join.ftmo.com/bgEkQxUhICPrkqGeDlOK) (Partner Code: `bgEkQxUhICPrkqGeDlOK`)

---

## 🧪 Run Local Backtesting Audit

Run the standalone Monte Carlo backtesting suite directly in your terminal (requires zero pip dependencies):

```bash
python3 strategies/python_liquidity_backtest.py
```

---

## 📜 Community & Open Source

- Star ⭐ this repo to support open quant development!
- Pull Requests for multi-asset backtest extensions (Forex, Crypto, CME Futures) are welcome.
- **Risk Disclaimer**: All software, models, and mathematical scripts are strictly for educational research. Algorithmic trading involves substantial capital risk.
