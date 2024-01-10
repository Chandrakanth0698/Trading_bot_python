# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:36:24 2024

@author: chand
"""

import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/META/financials?p=META"
headers = {"user-Agent": "Chrome/120.0.6099.13"}
page = requests.get(url,headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content,"html.parser")
table = soup.find_all("div",{"class":"table.svelte-1pgoo1f"})