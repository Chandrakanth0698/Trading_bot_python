# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:37:45 2024

@author: chand
"""

import yfinance as yf
#import pandas as pd
#import datetime as dt

tickers = ["AAPL","MSFT","GOOG","META","CSCO"]
ohlcv = {}
for ticker in tickers:
    temp = yf.download(ticker,period="1mo",interval="15m")
    temp.dropna(how="any",inplace = True)
    ohlcv[ticker] = temp
    

def MACD(DF,fast=12, slow=26, signal_len=9):
    """
    MACD - "Moving average Convergence Divergence"
    MACD(args) return the df with 2 additional colums
    "macd" and "signal"
    macd calculation:  MACD Line: (12-day EMA - 26-day EMA) 
    Signal Line: 9-day EMA of MACD Line
    MACD Histogram: MACD Line - Signal Line
    """
    df = DF.copy()
    df["ma_fast"] = df["Adj Close"].ewm(span=fast, min_periods=fast).mean()
    df["ma_slow"] = df["Adj Close"].ewm(span=slow, min_periods=slow).mean()
    df["macd"] = df["ma_fast"] - df["ma_slow"]
    df["signal"] = df["macd"].ewm(span=signal_len, min_periods=signal_len).mean()
    return df.loc[:,["macd","signal"]]

for ticker in ohlcv:
    ohlcv[ticker][["MACD","Signal"]] = MACD(ohlcv[ticker])
        
