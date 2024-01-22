# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:21:30 2024

@author: chand
"""

import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ["AMZN","MSFT","META","GOOG"]
start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()

cl_price = pd.DataFrame()
for ticker in tickers:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]

cl_price.dropna(axis=0, how="any",inplace=True)

cl_price.describe()
daily_return = cl_price.pct_change()
# ploting mean of daily returns
fig, ax = plt.subplots()
ax.set(title = "Mean Daily Returns",xlabel = "Stocks", ylabel = "Mean Returns")
plt.bar(x=daily_return.columns,height=daily_return.mean())
plt.bar(x=daily_return.columns,height=daily_return.std())
