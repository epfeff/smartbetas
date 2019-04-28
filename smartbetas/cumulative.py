# -*- coding: UTF-8 -*-
""":mod:`__cumulative__` is used to compute cumulative returns; also known as
momentum.

In this application, momentum is considered as the returns on a period between
12 months ago and 2 months ago.

All the date and time operations are handled with python's standard
`datetime` module.

.. _Python datetime:
   https://docs.python.org/3/library/datetime.html
"""
from datetime import datetime, timedelta

def ret(data):
    """ Computes the cumulative returns (momentum) of a security.

    Parameters:
        - `data` : :class:`list`  of :class:`tuples`

    Note: The function argument is built by :py:func:`api.tsd`, it is
    structured as follow: ``[(datetime.datetime(2019, 4, 18, 0, 0), 203.86)]`` .

    The function uses :mod:`__datetime__` to determine the dates between which
    the momentum shall be calculated. A new :class:`list` containing only the
    values to consider (the ones within the right time frame) is built and
    passed to :py:func:`cumulative.momentum`.

    Returns a the momentum of the security (:class:`float`)
    """
    vector = []
    today = datetime.today()
    delta1 = timedelta(weeks = 8)
    delta2 = timedelta(weeks = 52)
    two_m = today - delta1
    one_y = today - delta2
    # filters the list according to the date of the closing value
    for item in data:
        if item[0] <= two_m and item[0] >= one_y:
            vector.append(item[1])
    # computes the cumulative returns for the filtered list
    cmr = momentum(vector)
    return cmr

def momentum(vector):
    """ Computes the momentum of a vector.

    Parameters:
        - `vector` : :class:`list`  of :class:`floats`

    The function computes the returns of the data passed as argument:
        - momentum = 100*(new - old)/old

    Returns the momentum of the vector (:class:`float`)
    """
    return 100*((vector[0] - vector[-1])/vector[-1])
