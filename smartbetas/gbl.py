# -*- coding: UTF-8 -*-
""":mod:`__gbl__` is used to list/access/set variables with a global scope.

In this application we need to make some chunks of data available for multiple
modules, for this reason we use variables of a global scope. For the sake of
clarity, they are declared on a module dedicated to that.

The following global variables are declared:
    - `TICKERS`     :   :class:`list` storing tickers to compute
    - `NAMES`       :   :class:`list` storing `TICKERS`'s name
    - `P_VOL`       :   :class:`dict` storing the volatility portfolio
    - `P_CMR`       :   :class:`dict` storing the momentum portfolio
    - `P_CMP`       :   :class:`dict` storing the composite portfolio
    - `PRICES`      :   :class:`dict` storing the prices register
    - `API_KEY`     :   :class:`string` storing the API key
    - `API_URL`     :   :class:`string` storing the API URL

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
