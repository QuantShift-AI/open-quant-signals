# ⚡ QuantShift AI · Open-Source Algorithmic Trading Engines

[![YouTube Channel](https://img.shields.io/badge/YouTube-Watch%20Walkthroughs-red?style=for-the-badge&logo=youtube)](https://youtube.com/@aitrading)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![TradingView](https://img.shields.io/badge/TradingView-Verified%20Code-blue?style=for-the-badge&logo=tradingview)](https://www.tradingview.com/?aff_id=QuantShift)
[![GitHub Stars](https://img.shields.io/github/stars/AidenChan2025/open-quant-signals?style=for-the-badge&color=yellow)](https://github.com/AidenChan2025/open-quant-signals)

> **Zero paid courses. Zero paid VIP Discord groups. 100% free & open-source quant strategies.**  
> We mathematically expose how institutional algorithms hunt retail stop losses — and build open-source tools to trade alongside smart money.

---

## 📺 Video Walkthroughs (YouTube & TikTok)

- **EP01: Why 95% of Day Traders Get Hunted by Liquidity Sweeps**  
  [![Watch on YouTube](https://img.shields.io/badge/YouTube%20Shorts-Watch%20Now-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@aitrading)  
  *Watch how smart money bots engineer artificial breakouts to trigger retail stop losses, and how our PineScript code detects this in real-time.*

---

## 📦 Available Open-Source Engines

| Engine ID | Name | Platform | Win Rate (Backtested) | Profit Factor | Status |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **EP01** | [Liquidity Sweep Engine](./indicators/QuantShift_Liquidity_Sweep_Engine.pine) | TradingView (PineScript v5) | **64.2%** | **2.41** | ✅ Ready |
| **EP02** | Fair Value Gap (FVG) Momentum Matrix | PineScript / Python | *Coming soon* | *TBD* | 🚧 Building |
| **EP03** | Order Book Imbalance Hunter | Python / CCXT | *Coming soon* | *TBD* | 🚧 Building |

---

## 🚀 Quick Start (How to Add to TradingView in 30 Seconds)

1. Open [TradingView.com](https://www.tradingview.com/?aff_id=QuantShift) (Free account works);
2. Click on the **Pine Editor** tab at the bottom of any chart;
3. Copy the code from [`indicators/QuantShift_Liquidity_Sweep_Engine.pine`](./indicators/QuantShift_Liquidity_Sweep_Engine.pine);
4. Paste it into the editor and click **"Add to Chart"**;
5. Set alerts on your preferred symbols (EURUSD, BTCUSDT, SPY, etc.).

---

## 📊 EP01 Strategy Logic & Backtesting Mechanics

Retail traders place stop losses right below obvious swing lows. Institutional algorithms trigger a sudden price drop to absorb those sell orders at discount prices before rocketing the market upward.

- **Lookback**: 20 bars
- **Filter**: 1.5x ATR Volatility Envelope
- **Execution Rule**: Candle MUST pierce the liquidity pool but close back inside the range.

Detailed mathematical breakdown available in [`docs/EP01_Liquidity_Sweep_Breakdown.md`](./docs/EP01_Liquidity_Sweep_Breakdown.md).

---

## 🤝 Community & Disclaimer

- Star ⭐ this repository if you find it valuable!
- Contributions & Pull Requests for backtests are welcome.
- **Disclaimer**: All code and documentation are strictly for educational and backtesting research. Trading financial markets carries significant risk of capital loss.
