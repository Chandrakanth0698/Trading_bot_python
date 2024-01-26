# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:26:23 2024

@author: chand
"""

import yfinance as yf
import numpy as np
#import pandas as pd
#import datetime as dt

tickers = ["AAPL","MSFT","GOOG","META","CSCO"]
ohlcv = {}
for ticker in tickers:
    temp = yf.download(ticker,period="1mo",interval="5m")
    temp.dropna(how="any",inplace = True)
    ohlcv[ticker] = temp
    
def RSI(DF, n=14):
    """
    The Relative Strength Index (RSI) is a well versed momentum based 
    oscillator which is used to measure the speed (velocity) as well
    as the change (magnitude) of directional price movements. 

    """
    df = DF.copy()
    df["Change"] = df["Adj Close"] - df["Adj Close"].shift(1)
    df["Gain"] = np.where(df["Change"]>=0,df["Change"],0)
    df["Loss"] = np.where(df["Change"]<0,-(1)*df["Change"],0)
    df["avg_gain"] = df["Gain"].ewm(alpha = 1/n,min_periods = n).mean()
    df["avg_loss"] = df["Loss"].ewm(alpha = 1/n,min_periods = n).mean()
    df["rs"] = df["avg_gain"] / df["avg_loss"]
    df["RSI"] = 100 - (100/(1+df["rs"]))
    return df["RSI"]

for ticker in ohlcv:
    ohlcv[ticker]["RSI"]= RSI(ohlcv[ticker])