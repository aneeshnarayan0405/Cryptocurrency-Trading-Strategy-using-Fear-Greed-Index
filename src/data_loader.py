import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class DataLoader:
    def __init__(self, fear_greed_path, trades_path):
        self.fear_greed_path = fear_greed_path
        self.trades_path = trades_path
        
    def load_data(self):
        """Load and preprocess the raw data"""
        fear_greed = pd.read_csv(self.fear_greed_path)
        trades = pd.read_csv(self.trades_path)
        
        # Convert date columns
        fear_greed['date'] = pd.to_datetime(fear_greed['date'])
        trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], dayfirst=True)
        trades['date'] = trades['Timestamp IST'].dt.date
        trades['date'] = pd.to_datetime(trades['date'])
        
        # Clean and sort data
        fear_greed = fear_greed.sort_values('date').reset_index(drop=True)
        
        # Process numeric columns
        numeric_cols = ['Execution Price', 'Size Tokens', 'Size USD', 'Closed PnL', 'Fee']
        trades[numeric_cols] = trades[numeric_cols].apply(pd.to_numeric, errors='coerce')
        
        # Create trading direction column
        trades['Direction'] = trades['Side'].apply(lambda x: 1 if x == 'BUY' else -1)
        trades['Cumulative_Tokens'] = trades.groupby('Coin')['Size Tokens'].cumsum()
        
        return fear_greed, trades
    
    def merge_data(self, fear_greed, trades):
        """Merge the fear/greed and trading data"""
        merged_data = pd.merge(trades, fear_greed, on='date', how='left')
        
        # Create sentiment categories
        def get_sentiment_category(value):
            if pd.isna(value):
                return 'Unknown'
            elif value >= 75:
                return 'Extreme Greed'
            elif value >= 55:
                return 'Greed'
            elif value >= 45:
                return 'Neutral'
            elif value >= 25:
                return 'Fear'
            else:
                return 'Extreme Fear'
            
        merged_data['Sentiment'] = merged_data['value'].apply(get_sentiment_category)
        
        return merged_data
