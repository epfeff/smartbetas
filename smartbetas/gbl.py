# -*- coding: UTF-8 -*-

TICKERS = []                               # list of item to compute
NAMES = []                                 # list of company names from TICKERS
P_MAX = 10                                 # investment portfolio max size
P_VOL = {}
P_CMR = {}
P_CMP = {}
PRICES = {}
API_KEY='K44NPIPA1JQK6QGM'
API_URL=('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&\
symbol=%s&outputsize=full&apikey=%s')
