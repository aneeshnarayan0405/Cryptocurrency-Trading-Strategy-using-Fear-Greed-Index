# 📁 Outputs Folder

This folder contains the result files generated after strategy simulation, performance evaluation, and backtesting.

## 📄 CSV Files

| Filename                          | Description |
|----------------------------------|-------------|
| `coin_performance_metrics.csv`   | Contains performance metrics (e.g., Sharpe Ratio, CAGR, Max Drawdown) calculated individually for each cryptocurrency coin under various trading strategies. Useful for coin-level comparison. |
| `portfolio_performance_metrics.csv` | Contains aggregate portfolio metrics across all coins for each trading strategy. This file summarizes overall performance including total returns, average volatility, and drawdown. |

---

## 📈 Usage

You can load these CSVs in your Python notebooks or scripts to:
- Compare which **coin performs best** under different strategies.
- Analyze which **strategy performs best overall** on a portfolio level.
- Plot charts, rank strategies, or use for reporting.

### Example:

```python
import pandas as pd

coin_metrics = pd.read_csv("outputs/coin_performance_metrics.csv")
portfolio_metrics = pd.read_csv("outputs/portfolio_performance_metrics.csv")

print(coin_metrics.head())
print(portfolio_metrics.head())
