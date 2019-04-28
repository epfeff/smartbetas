# -*- coding: UTF-8 -*-
""":mod:`__money__` is handle investments in the computed portfolios.

In the application, when a user requested to compute portfolios based on the
tickers he provided, he can choose to invest money in the portfolios to be
able to check them later on.

For now one can only invest 100'000 USD in each portfolio with a reparatition
of 1/n where n is the amount of tickers in a portfolio.
"""
from db import db
from datetime import datetime, date, timedelta

def invest(p_size, p_vol, p_cmr, p_cmp, prices, s_name, stack=100000):
    """ Invests 100'000 USD in each computed portfolio.

    Parameters:
        - `p_size` : :class:`int` amount of tickers per portfolio.
        - `p_vol`  : :class:`dict` volatility portfolio.
        - `p_cmr`  : :class:`dict` momentum portfolio.
        - `p_cmp`  : :class:`dict` composite portfolio.
        - `prices` : :class:`dict` price register.
        - `s_name` : :class:`string` name of the investment.
        - `stack`  : :class:`ìnt` defaults to 100000, money to invest.

    For each portfolio, the function determines to max amount of shares that
    can be purchased and builds a :class:`dict` of tickers and quantity of
    shares.

    The function then stores the outcomes into the database, the prices of the
    securities are also stored for future usage.

    Returns nothing.
    """
    inv_vol = {}                    # investment on volatility portfolio
    inv_cmr = {}                    # investment on cumulative return portfolio
    inv_cmp = {}                    # investment on composite portfolio
    sec_inv = stack / p_size        # money to invest in each security
    inv_prc = {}                    # investment's price register
    for i, j in enumerate(p_vol.keys()):
        if i < p_size:
            inv_vol[j] = round(sec_inv/prices[j])
            inv_prc[j] = prices[j]
    for i, j in enumerate(p_cmr.keys()):
        if i < p_size:
            inv_cmr[j] = round(sec_inv/prices[j])
            inv_prc[j] = prices[j]
    for i, j in enumerate(p_cmp.keys()):
        if i < p_size:
            inv_cmp[j] = round(sec_inv/prices[j])
            inv_prc[j] = prices[j]
    db.investments.insert(  date = datetime.now(),
                            name = s_name,
                            vol = inv_vol,
                            cmr = inv_cmr,
                            cmp = inv_cmp,
                            prc = inv_prc)
    db.commit()
