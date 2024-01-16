# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:36:24 2024

@author: chand
"""

import requests
from bs4 import BeautifulSoup

tickers = ["AAPL","META","CSCO","INFY.NS","3988.HK"]
income_stmt_dict = {}
balance_sheet = {}
cashflow_sheet = {}

for  ticker in tickers:
    url = f"https://finance.yahoo.com/quote/META/financials?p={ticker}"
    income_stmt = {}
    table_title = {}
    headers = {"user-Agent": "Chrome/120.0.6099.13"}
    page = requests.get(url,headers=headers)
    page_content = page.content
    #print(page_content)
    soup = BeautifulSoup(page.content,"html.parser")
    table = soup.find_all("div",{"class":"M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in table:
        heading = t.findall("div",{"class":"D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator = "|").split("|")[0]]= top_row.get_text(separator = "|")[1:]
        rows = t.find_all("div",{"class":"D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            income_stmt[row.get_text(separator = "|").split("|")[0]] = row.get_text(separator = "|")[1:]
