import pandas as pd
import numpy as np

class TradingStrategies:
    def __init__(self, merged_data):
        self.data = merged_data
        
    def contrarian_strategy(self):
        """Buy when fear, sell when greed"""
        signals = []
        current_position = 0
        
        for idx, row in self.data.iterrows():
            sentiment = row['Sentiment']
            price = row['Execution Price']
            
            if sentiment in ['Extreme Fear', 'Fear'] and current_position <= 0:
                # Buy signal
                signals.append(1)
                current_position = 1
            elif sentiment in ['Extreme Greed', 'Greed'] and current_position >= 0:
                # Sell signal
                signals.append(-1)
                current_position = -1
            else:
                signals.append(0)
                
        self.data['Contrarian_Signal'] = signals
        return self.data
    
    def momentum_strategy(self, window=7):
        """Follow the trend when sentiment is strong"""
        self.data['Price_Change'] = self.data.groupby('Coin')['Execution Price'].pct_change(window)
        signals = []
        
        for idx, row in self.data.iterrows():
            sentiment = row['Sentiment']
            price_change = row['Price_Change']
            
            if sentiment in ['Extreme Greed', 'Greed'] and price_change > 0:
                signals.append(1)  # Buy
            elif sentiment in ['Extreme Fear', 'Fear'] and price_change < 0:
                signals.append(-1)  # Sell
            else:
                signals.append(0)  # Hold
                
        self.data['Momentum_Signal'] = signals
        return self.data
    
    def calculate_returns(self, signal_col):
        """Calculate returns for a given signal column"""
        self.data['Strategy_Return'] = self.data[signal_col] * self.data['Execution Price'].pct_change()
        self.data['Cumulative_Return'] = (1 + self.data['Strategy_Return']).cumprod()
        return self.data
