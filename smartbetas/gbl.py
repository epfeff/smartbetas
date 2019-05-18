# -*- coding: UTF-8 -*-
""":mod:`gbl.py` is used to list/access/set variables with a global scope.
"""

TICKERS = []                               # list of item to compute
NAMES = []                                 # list of company names from TICKERS
P_VOL = {}                                 # volatility portfolio
P_CMR = {}                                 # momentum portfolio
P_CMP = {}                                 # composite portfolio
PRICES = {}                                # prices register
API_KEY='K44NPIPA1JQK6QGM'                 # public API key
API_URL=('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&\
symbol=%s&outputsize=full&apikey=%s')      # public API URL
