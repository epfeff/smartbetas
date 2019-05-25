# -*- coding: UTF-8 -*-
""":mod:`volatility.py` is used to compute the volatility of a stock.
"""
from statistics import stdev
from datetime import datetime, timedelta

def volatility(data):
    """ Computes the volatility of a stock.

    Parameters:

        - `data` : :class:`list`  of :class:`tuples`

    .. note::
      The function's argument is provided by :py:func:`api.tsd`, each item in
      this list is structured as follow:
      ``[(datetime.datetime(2019, 4, 18, 0, 0), 203.86)]``

    The function uses :mod:`datetime` to determine the dates between which
    the volatility shall be computed. A new :class:`list` in which the daily
    returns between the right time frame is built.

    We then use `statistics.stdev` to compute the standard deviation of the list.

    Returns a the volatility of the security (:class:`float`)
    """
    # select only last two years
    vector = []
    today = datetime.today()
    delta = timedelta(weeks = 104)
    two_y = today - delta               # date two years ago

    for i, item in enumerate(data):
        if item[0] >= two_y:
            vector.append(item[1]/data[i-1][1]*100)
    vector[0] = 0
    return stdev(vector)
