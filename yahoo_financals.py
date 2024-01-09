# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:57:34 2024

@author: chand
"""

import pandas as pd
from yahoofinancials import YahooFinancials
import datetime as dt

all_tickers = ['AMZN', 'MSFT', 'INTC', 'GOOG']

# extracting stock data

close_prices = pd.DataFrame()
end_date = (dt.date.today()).strftime("%Y-%m-%d")
start_date =(dt.date.today()-dt.timedelta(1825)).strftime("%Y-%m-%d")
for ticker in all_tickers:
    yahoo_fin = YahooFinancials(ticker)
    json_obj = yahoo_fin.get_historical_price_data(start_date,end_date,"daily")
    ohlv = json_obj[ticker]["prices"]
    temp = pd.DataFrame(ohlv)[["formatted_date","adjclose"]]
    temp.set_index("formatted_date",inplace = True)
    temp.dropna(inplace=True)
    close_prices[ticker] = temp["adjclose"]