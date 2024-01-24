# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:37:45 2024

@author: chand
"""

import yfinance as yf
import pandas as pd
import datetime as dt

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
    macd is calculated as the difference between simple
    """
    df = DF.copy()
    d