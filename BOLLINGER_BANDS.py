# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:54:52 2024

@author: chand
"""

import yfinance as yf
#import pandas as pd
#import datetime as dt

tickers = ["AAPL","MSFT","GOOG","META","CSCO"]
ohlcv = {}
for ticker in tickers:
    temp = yf.download(ticker,period="1mo",interval="5m")
    temp.dropna(how="any",inplace = True)
    ohlcv[ticker] = temp
    
def BOLLINGER_BANDS(DF,n=20):
    """
    Bolliner bands are a set of 3 band, its a lagging indicator used to measure
    volatility, The line in the middle is usually a Simple Moving Average (SMA)
    set to a period of 20 days, The Upper and Lower Bands are used as a way to
    measure volatility by observing the relationship between the 
    Bands and price.
    Calculation:
        middle line - 20 day SMA(Simple moving Avg)
        upper line - 20 day SMA + (Standard deviation x 2)
        lower line - 20 day SMA - (Standard deviation x 2)
    """
    df = DF.copy()
    df["Middle_line"] = df["Adj Close"].rolling(n).mean()
    df["Upper_line"] = df["Middle_line"] + (df["Adj Close"].std()*2)
    df["Lower_line"] = df["Middle_line"] - (df["Adj Close"].std()*2)
    df["Band_width"]= df["Upper_line"] - df["Lower_line"]
    return df[["Middle_line","Upper_line","Lower_line","Band_width"]]

for ticker in ohlcv:
    ohlcv[ticker][["Middle_line","Upper_line","Lower_line","Band_width"]] = BOLLINGER_BANDS(ohlcv[ticker])
    