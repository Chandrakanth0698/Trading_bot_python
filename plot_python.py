# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:42:08 2024

@author: chand
"""

import datetime as dt
import yfinance as yf
import pandas as pd

tickers = ["AMZN","MSFT","META","GOOG"]
start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()

cl_price = pd.DataFrame()
for ticker in tickers:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]

cl_price.dropna(axis=0, how="any",inplace=True)

cl_price.describe()
daily_return = cl_price.pct_change()
cl_price.plot()
cl_price.plot(subplots = True,layout = (2,2),title = "Stock price Evolution", grid = True)
daily_return.plot(subplots = True, layout=(2,2),title="Daily Returns")
(1+daily_return).cumprod()

(1+daily_return).cumprod().plot()
