# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:20:01 2024

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
    
def ATR(DF,length=14):
    """
    ATR = average true range
    it is a volatility indicator especially volatility caused by price gaps or limit moves.
    calculation:
        True range = max(current_high - current_low, abs(curr_high - prev_close), abs(curr_close - prev_close))
        then we take exponential moving avg for true range to get avg of the True Range(EMA)
    """
    df= DF.copy()
    df["cur_delta"] = df["High"] - df["Low"]
    df["abs_hc"] = abs(df["High"] - df["Adj Close"].shift(1))
    df["abs_cc"] = abs(df["Close"] - df["Close"].shift(1))
    df["TR"] = df[["cur_delta","abs_cc","abs_hc"]].max(axis = 1,skipna = False)
    df["ATR"] = df["TR"].ewm(span=length, min_periods=length).mean()
    return df["ATR"]

for ticker in ohlcv:
    ohlcv[ticker]["ATR"] = ATR(ohlcv[ticker])