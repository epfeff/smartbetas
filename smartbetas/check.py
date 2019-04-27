# -*- coding: UTF-8 -*-
""":mod:`__check__` is used to determine the returns of an investment.

This module fetches from the stock data API today's securities values and
compares them with the data from a previous investment session stored in the
database. (API data provided through :api:`api.tsd`)

To expedite things, this module uses python's `concurrent.futures` to fetch
data from the API in a parallel fashion. This is done to save time as `HTTP`
requests take time no matter how poweful the host running the code is.

.. _Python ``concurrent.futures``:
   https://docs.python.org/3/library/concurrent.futures.html
"""
import api
import concurrent.futures
from db import db
from datetime import datetime

def sessions(id):
    """ Determines returns of an investment session.

    Parameters:
        - `id` : :class:`integer`  investment session database id.

    Uses ``ProcessPoolExecutor`` to request in parallel the latest prices of
    each tickers using :get_price:`check.get_price` and stores the results in
    a :class:`dict` :  ``{'ticker1': 100, 'ticker2': 200}.

    The returns of the portfolios are calculated by :returns:`check.returns`.

    Once the returns are calculated, the results are saved in the database, this
    is to allow users to consults the results later on without having the
    re-compute the returns or query any data from the API.

    Returns:
        - `r_vol`       : :class:`dict`  Returns of the volability portfolio.
        - `r_cmr`       : :class:`dict`  Returns of the momentum portfolio.
        - `r_cmp`       : :class:`dict`  Returns of the composite portfolio.
        - `inv['name']` : :class:`string`  investment session name.
    """
    r_vol = {}                      # returns on the volability portfolio
    r_cmr = {}                      # returns on the cumulative return pf
    r_cmp = {}                      # returns on the composite portfolio

    n_prices = []                   # ticker prices dictionnary
    # gets data from the database
    inv = db(db.investments.id == id).select().as_list()[0]
    # creates a list of the tickers listed in the db row
    tickers = list(inv['prc'].keys())
    # gets the current price of all the tickers listed in the db row
    with concurrent.futures.ProcessPoolExecutor() as executor:
        n_prices = list(executor.map(get_price, tickers))
    # generates a dict {tickers: prices}
    n_prices = {x[0]:x[1] for x in n_prices}
    # gets returns from each portfolio
    r_vol = returns(inv, 'vol', n_prices)
    r_cmr = returns(inv, 'cmr', n_prices)
    r_cmp = returns(inv, 'cmp', n_prices)
    # saves the outcome in the database for future usage
    db.checks.insert(       date = str(datetime.now())[:10],
                            name = inv['name'],
                            vol = r_vol,
                            cmr = r_cmr,
                            cmp = r_cmp)
    db.commit()
    # returns the returns and the name of the investment
    return r_vol, r_cmr, r_cmp, inv['name']

def get_price(tick):
    """ Gets the current price of a security.

    Parameters:
        - `tick` : :class:`string`  security ticker

    Fetches the latest price of the ticker from the stock api. The result is
    stored in a :class:`tuple` : ```('ticker', 149)``

    Returns a :class:`tuple` containing the ticker and its latest price.
    """
    data = api.tsd(tick)
    price = (tick, data[0][1])
    return price

def returns(inv, pfl, prices):
    """ Computes the return of a portfolio.

    Parameters:
        - `inv`     : :class:`list` past investment session row from the db
        - `pfl`     : :class:`string` name of the portfolio
        - `prices`  : :class:`dict` latest investment's ticker prices

    Computes the absolute change and the returns for each ticker in the
    portfolio. These values are calculated as follow:
        - Absolute change : (qty *new) - (qty * old) (*rounded at 2 digits*)
        - Returns         : [(new-old)/old*100] (*rounded at 2 digits*)

    The total absolute change and return is handled by
    :t_returns:`check.t_returns`.

    Returns a :class:`dict` containing for each ticker the initial price,
    the new price, the absolute change, the returns, the quantity of shares and
    the date of the purchase.
    """
    out = dict()
    for t in list(inv[pfl].keys()):
        new = prices[t]
        old = inv['prc'][t]
        qty = inv[pfl][t]
        date = inv['date']
        out[t] = dict()
        out[t]['old'] = old
        out[t]['new'] = new
        out[t]['abs'] = round((qty *new) - (qty * old), 2)
        out[t]['rel'] = round((((new - old) / old) * 100), 2)
        out[t]['qty'] = qty
        out[t]['date'] = date
    out['Total'] = t_returns(inv, pfl, prices, date)
    return out

def t_returns(inv, pfl, prices, date):
    """ Computes the total return of a portfolio.

    Parameters:
        - `inv`     : :class:`list` past investment session row from the db
        - `pfl`     : :class:`string` name of the portfolio
        - `prices`  : :class:`dict` latest investment's ticker prices
        - `date`    : :class:`string` date of the purchase

    Computes the sum of the initial portfolio value and the sum of the current
    portfolio value. Based on the sums, it computes the absolute change and the
    returns using the same formula as in :returns:`check.returns`.

    Returns a :class:`dict` containing the total initial price, the new
    price, the absolute change, the returns and the date of the purchase.
    """
    t_old = sum(map(lambda key: inv[pfl][key]*inv['prc'][key], inv[pfl].keys()))
    t_old = round(t_old, 1)
    t_new = sum(map(lambda key: inv[pfl][key]*prices[key], inv[pfl].keys()))
    t_new = round(t_new, 1)
    abs = round(t_new - t_old, 1)
    rel = round(((t_new - t_old) / t_old) * 100, 2)
    return {'abs': abs, 'rel': rel, 'old': t_old,
        'new': t_new, 'qty': 'NA', 'date': date}
