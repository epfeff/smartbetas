# -*- coding: UTF-8 -*-
""":mod:`money.py` handles investments in the computed portfolios.
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

    In each portfolio, the function determines how many shares of stock can
    be purchased. A :class:`dict` containing the stocks and the quantity of
    shares purchased is built.

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
