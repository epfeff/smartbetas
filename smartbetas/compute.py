# -*- coding: UTF-8 -*-
""":mod:`__compute__` is used to compute volatility, momentum and composite
based porfolio.

This module gets from the stock data API the security closing value and
computes for each security the volatility and the momentum.

Based on the security ranking it also computes a composite portfolio.

To expedite things, this module uses python's `concurrent.futures` to fetch
data from the API in a parallel fashion. This is done to save time as `HTTP`
requests take time no matter how poweful the host running the code is.

.. _Python ``concurrent.futures``:
   https://docs.python.org/3/library/concurrent.futures.html
"""
import api, json,concurrent.futures
import volatility, cumulative, composite, i_o, gbl
from threading import Thread

def smartbetas(tickers):
    """ Builds three portfolios based on volatility, momentum and a composite
    score.

    Parameters:

        - `tickers` : :class:`list`  of tickers to compute

    Uses ``ProcessPoolExecutor`` to perform for each ticker the following tasks
    in parallel (using the function :py:func:`compute.compute`):

        - Get data from the web API - :py:func:`api.tsd`
        - Compute volatility - :py:func:`volatility.volatility`
        - Compute momentum - :py:func:`cumulative.ret`

    The output of the parallel processing is stored in a :class:`list`
    containing for each ticker a :class:`list` of :class:`tuples`.

    Sample:

        .. code-block:: python

            [[('t1', volatility), ('t1', momentum), ('t1', price)],
                [('t2', vol), ('t2', vol), ('t2', vol)]]

    The volability portfolio is built by sorting the :class:`list` in an
    ascending fashion and extracting only the tickers and their volatility.

    The momentum portfolio is built by sorting the :class:`list` in a
    descending fashion and extracting the tickers and their momentum.

    The prices are also extracted to allow for future comparisons against the
    market prices.

    The composite portfolio is computed with :py:func:`composite.composite`.

    The results are stored in the global variables.

    Returns nothing
    """
    p_vol = {}                      # portfolio volatility
    p_cmr = {}                      # portfolio cumulative
    p_cmp = {}                      # portfolio composite
    v_r_p = []                      # volability, return and prices map

    # paralel processing of the computing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        v_r_p = list(executor.map(compute, tickers))
    # sorts into two dicts
    v_r_p.sort(key = lambda x: x[0][1])
    p_vol = {x[0][0]:x[0][1] for x in v_r_p}
    v_r_p.sort(key = lambda x: x[1][1], reverse = True)
    p_cmr = {x[1][0]:x[1][1] for x in v_r_p}
    prices = {x[2][0]:x[2][1] for x in v_r_p}
    # composite vector
    p_cmp = composite.composite(p_vol, p_cmr)
    # display table of outputs
    i_o.portfolio(p_vol, p_cmr, p_cmp, prices)
    # stores the outome in the global variables
    gbl.P_VOL = p_vol
    gbl.P_CMR = p_cmr
    gbl.P_CMP = p_cmp
    gbl.PRICES = prices

def compute(tick):
    """ Returns the volatility, momentum and price of a ticker.

    This function gets the tickers data with the :py:func:`api.tsd`, the volatility
    with :py:func:`volatility.volability` and the momentum with the module
    :py:func:`cumulative.ret`.

    These function calls are segregated into this function to enable parallel
    processing.

    Returns a :class:`list` containing the volatility, the momentum and the
    price of a ticker.
    """
    data = api.tsd(tick)
    price = (tick, data[0][1])
    vol = (tick, volatility.volatility(data))
    cmr = (tick, cumulative.ret(data))
    return [vol, cmr, price]
