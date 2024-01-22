# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:17:36 2024

@author: chand
"""

import datetime as dt
import yfinance as yf
import pandas as pd

tickers = ["AMZN","MSFT","META","GOOG"]
start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()

cl_price = pd.DataFrame()
# looping over tickers and filling data with closeprices of tickers
for ticker in tickers:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]

cl_price['AAPL'] = yf.download('AAPL', start, end)["Adj Close"]

# dropping NaN values
cl_price.dropna(axis=0, how="any",inplace=True)

cl_price.describe()
daily_return = cl_price.pct_change()
# percentage change 
# daily_return = cl_price/cl_price.shift(1)

daily_return.describe()
cl_price.plot()
daily_return.plot()
# to get a window of values
daily_return.rolling(window=10).mean().head(11)
