import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

class Visualizer:
    def __init__(self):
        plt.style.use('seaborn')
        plt.rcParams['figure.figsize'] = [12, 6]
        
    def plot_sentiment_timeline(self, fear_greed):
        """Plot the Fear & Greed Index timeline with sentiment zones"""
        plt.figure(figsize=(16, 8))
        plt.plot(fear_greed['date'], fear_greed['value'], label='Index Value', color='navy')
        
        # Add sentiment zones
        plt.axhspan(0, 25, color='green', alpha=0.1, label='Extreme Fear')
        plt.axhspan(25, 45, color='lightgreen', alpha=0.1, label='Fear')
        plt.axhspan(45, 55, color='lightgray', alpha=0.1, label='Neutral')
        plt.axhspan(55, 75, color='lightcoral', alpha=0.1, label='Greed')
        plt.axhspan(75, 100, color='red', alpha=0.1, label='Extreme Greed')
        
        plt.title('Fear & Greed Index Timeline with Sentiment Zones')
        plt.ylabel('Index Value')
        plt.xlabel('Date')
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.show()
        
    def plot_trading_volume(self, merged_data):
        """Plot daily trading volume over time"""
        plt.figure(figsize=(14, 7))
        daily_volume = merged_data.groupby('date')['Size USD'].sum()
        daily_volume.plot()
        plt.title('Daily Trading Volume Over Time')
        plt.ylabel('Total Trading Volume (USD)')
        plt.grid(True)
        plt.show()
        
    def plot_coin_distribution(self, merged_data):
        """Plot distribution of trades by coin"""
        plt.figure(figsize=(12, 6))
        coin_dist = merged_data['Coin'].value_counts(normalize=True) * 100
        coin_dist.plot(kind='bar')
        plt.title('Distribution of Trades by Coin (%)')
        plt.ylabel('Percentage of Trades')
        plt.xticks(rotation=45)
        plt.show()
        
    def plot_sentiment_distribution(self, merged_data):
        """Plot number of trades by market sentiment"""
        plt.figure(figsize=(10, 6))
        sentiment_counts = merged_data['Sentiment'].value_counts().sort_index()
        ax = sentiment_counts.plot(kind='bar')
        plt.title('Number of Trades by Market Sentiment')
        plt.ylabel('Count')
        
        # Add value annotations
        for p in ax.patches:
            ax.annotate(f'{p.get_height():,.0f}',
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center',
                        xytext=(0, 5),
                        textcoords='offset points')
        plt.show()
        
    def plot_strategy_performance(self, strategy_data, strategy_name):
        """Plot cumulative returns of a strategy"""
        plt.figure(figsize=(14, 7))
        plt.plot(strategy_data['date'], strategy_data['Cumulative_Return'], 
                label=f'{strategy_name} Strategy')
        plt.title(f'{strategy_name} Strategy Performance')
        plt.ylabel('Cumulative Returns')
        plt.xlabel('Date')
        plt.legend()
        plt.grid(True)
        plt.show()
