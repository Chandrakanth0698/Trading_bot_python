# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:38:39 2024

@author: chand
"""
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time
""" extracting for single ticker
ts = TimeSeries(key=open("D:\Quant\key.txt",'r').read(), output_format='pandas')
data = ts.get_daily(symbol='GOOGL',outputsize="full")[0]
data.columns = ["open","high","low","close","volume"]
"""

all_stocks = ["AMZN","MSFT","INTC","GOOG","CSCO","META"]
api_call_count = 0
close_price = pd.DataFrame()
for ticker in all_stocks:
    start_time = time.time()
    ts = TimeSeries(key=open("D:\Quant\key.txt",'r').read(), output_format='pandas')
    api_call_count += 1
    data = ts.get_daily(symbol=ticker,outputsize="full")[0]
    data.columns = ["open","high","low","close","volume"]
    close_price[ticker] = data["close"]
    if api_call_count == 5:
        api_call_count = 0
        time.sleep(time.time() - start_time)

close_price = close_price.iloc[::-1]
close_price.fillna()