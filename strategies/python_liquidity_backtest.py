"""
QuantShift AI · EP01 Python Liquidity Sweep Backtest Template
100% Free & Open Source | https://github.com/QuantShift-AI/open-quant-signals
"""

import pandas as pd
import numpy as np

def detect_liquidity_sweeps(df: pd.DataFrame, lookback: int = 20, atr_mult: float = 1.5):
    """
    df must contain columns: ['open', 'high', 'low', 'close']
    """
    df = df.copy()
    
    # Calculate Swing Highs & Lows
    df['prev_high'] = df['high'].shift(1).rolling(window=lookback).max()
    df['prev_low'] = df['low'].shift(1).rolling(window=lookback).min()
    
    # Calculate ATR
    df['tr'] = np.maximum(
        df['high'] - df['low'],
        np.maximum(
            abs(df['high'] - df['close'].shift(1)),
            abs(df['low'] - df['close'].shift(1))
        )
    )
    df['atr'] = df['tr'].rolling(window=14).mean()
    
    # Signals
    # Bullish Sweep: Low pierced below support, but Close finished above support
    df['bullish_sweep'] = (
        (df['low'] < df['prev_low']) & 
        (df['close'] > df['prev_low']) & 
        ((df['prev_low'] - df['low']) < (df['atr'] * atr_mult))
    )
    
    # Bearish Sweep: High pierced above resistance, but Close finished below resistance
    df['bearish_sweep'] = (
        (df['high'] > df['prev_high']) & 
        (df['close'] < df['prev_high']) & 
        ((df['high'] - df['prev_high']) < (df['atr'] * atr_mult))
    )
    
    return df

if __name__ == "__main__":
    print("QuantShift AI · Liquidity Sweep Engine loaded successfully.")
    print("Import `detect_liquidity_sweeps(df)` into your algorithmic backtesting pipeline.")
