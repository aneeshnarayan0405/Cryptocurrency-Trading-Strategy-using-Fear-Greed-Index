# Cryptocurrency-Trading-Strategy-using-Fear-Greed-Index

# 📈 Cryptocurrency Sentiment-Based Trading Strategy

This project presents a backtested cryptocurrency trading strategy using market sentiment data from the **Fear & Greed Index**. The strategy explores how psychological market states (fear and greed) affect crypto price action — and how traders can exploit these emotional extremes to design smarter trades.

---

## 🧠 Overview

- 📊 **Sentiment Source**: Alternative.me's Crypto Fear & Greed Index  
- 🪙 **Trade Data**: Historical trade logs from user portfolios  
- ⚙️ **Method**: Merging, preprocessing, EDA, signal generation, backtesting  
- 🔁 **Strategies**:
  - Contrarian (buy in fear, sell in greed)
  - Momentum (follow the crowd)
  - Neutral (hold during uncertain sentiment)

---

## 📘 Key Components

All the logic is implemented in a single Jupyter Notebook:  
📄 `Cryptocurrency_Trading_Strategy_using_Fear_&_Greed_Index.ipynb`

It includes:

- ✅ Data loading and cleaning
- 📊 Exploratory visualizations:
  - Sentiment trends
  - Trading volumes
  - Coin-wise distribution
- 📈 Signal generation based on sentiment classification
- 🧪 Backtesting strategy returns
- 📉 Portfolio-level evaluation
- 📦 Output of performance metrics to `.csv`

---

## 📊 Visualizations & Analysis

The notebook includes the following graphs:

- 📉 Fear & Greed Index over time
- 📈 Daily trading volume of portfolio
- 🪙 Coin-wise trade distribution
- 🧾 Cumulative strategy returns vs. Buy-and-Hold
- 🔻 Drawdown charts
- 💹 Comparison of different strategy types

All plots are generated using `matplotlib` and `seaborn`, and displayed directly in the notebook.

---

## 📂 Outputs

Results are saved in the `outputs/` folder:

| Filename                          | Description |
|----------------------------------|-------------|
| `coin_performance_metrics.csv`   | Metrics (CAGR, Sharpe Ratio, Max Drawdown, etc.) per coin per strategy |
| `portfolio_performance_metrics.csv` | Aggregated portfolio-level strategy performance |


