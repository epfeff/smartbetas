# -*- coding: UTF-8 -*-
""":mod:`__volatility__` is used to compute the volatility of a security.

In this application, momentum is considered on a period between two years ago
and now.

To calculate the volatility, a standard deviation needs to be performed. To do
so we use the standard python's statistics package.

.. _Python statistics:
   https://docs.python.org/3/library/statistics.html
"""
from statistics import stdev
from datetime import datetime, timedelta

def volatility(data):
    """ Computes the volatility of a security.

    Parameters:

        - `data` : :class:`list`  of :class:`tuples`

    Note: The function argument is built by :py:func:`api.tsd`, it is
    structured as follow: ``[(datetime.datetime(2019, 4, 18, 0, 0), 203.86)]`` .

    The function uses :mod:`__datetime__` to determine the dates between which
    the volatility shall be calculated. A new :class:`list` containing only the
    values to consider (the ones within the right time frame). The constructed
    list is then passed to `statistics.stdev` to compute the deviation.

    Returns a the volatility of the security (:class:`float`)
    """
    # select only last two years
    vector = []
    today = datetime.today()
    delta = timedelta(weeks = 104)
    two_y = today - delta               # date two years ago

    for item in data:
        if item[0] >= two_y:
            vector.append(item[1])
    return stdev(vector)
