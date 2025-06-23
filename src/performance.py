import numpy as np
import pandas as pd
from scipy import stats

class PerformanceMetrics:
    @staticmethod
    def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
        """Calculate annualized Sharpe ratio"""
        excess_returns = returns - risk_free_rate
        return np.sqrt(252) * excess_returns.mean() / excess_returns.std()
    
    @staticmethod
    def calculate_max_drawdown(cumulative_returns):
        """Calculate maximum drawdown"""
        peak = cumulative_returns.expanding(min_periods=1).max()
        drawdown = (cumulative_returns - peak) / peak
        return drawdown.min()
    
    @staticmethod
    def calculate_sortino_ratio(returns, risk_free_rate=0.0):
        """Calculate annualized Sortino ratio"""
        excess_returns = returns - risk_free_rate
        downside_returns = returns.copy()
        downside_returns[downside_returns > risk_free_rate] = 0
        downside_std = downside_returns.std()
        return np.sqrt(252) * excess_returns.mean() / downside_std
    
    @staticmethod
    def calculate_win_rate(returns):
        """Calculate percentage of profitable trades"""
        return len(returns[returns > 0]) / len(returns)
    
    @staticmethod
    def calculate_metrics(strategy_returns, benchmark_returns=None):
        """Calculate all performance metrics"""
        metrics = {
            'Annualized Return': np.prod(1 + strategy_returns)**(252/len(strategy_returns)) - 1,
            'Annualized Volatility': strategy_returns.std() * np.sqrt(252),
            'Sharpe Ratio': PerformanceMetrics.calculate_sharpe_ratio(strategy_returns),
            'Sortino Ratio': PerformanceMetrics.calculate_sortino_ratio(strategy_returns),
            'Max Drawdown': PerformanceMetrics.calculate_max_drawdown((1 + strategy_returns).cumprod()),
            'Win Rate': PerformanceMetrics.calculate_win_rate(strategy_returns)
        }
        
        if benchmark_returns is not None:
            metrics['Alpha'], metrics['Beta'] = PerformanceMetrics.calculate_alpha_beta(
                strategy_returns, benchmark_returns)
            metrics['Information Ratio'] = PerformanceMetrics.calculate_information_ratio(
                strategy_returns, benchmark_returns)
            
        return metrics
    
    @staticmethod
    def calculate_alpha_beta(strategy_returns, benchmark_returns):
        """Calculate alpha and beta relative to benchmark"""
        covariance = np.cov(strategy_returns, benchmark_returns)
        beta = covariance[0, 1] / covariance[1, 1]
        alpha = strategy_returns.mean() - beta * benchmark_returns.mean()
        return alpha, beta
    
    @staticmethod
    def calculate_information_ratio(strategy_returns, benchmark_returns):
        """Calculate information ratio"""
        active_return = strategy_returns - benchmark_returns
        return np.sqrt(252) * active_return.mean() / active_return.std()
