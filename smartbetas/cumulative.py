# -*- coding: UTF-8 -*-
""":mod:`cumulative.py` is used to compute cumulative returns; also known as
momentum.
"""
from datetime import datetime, timedelta

def ret(data):
    """ Computes the cumulative returns (momentum) of a security.

    Parameters:
        - `data` : :class:`list`  of :class:`tuples`

    .. note::
      The function argument is built by :py:func:`api.tsd`, it is
      structured as follow: ``[(datetime.datetime(2019, 4, 18, 0, 0), 203.86)]`` .

    The function uses :mod:`datetime` to determine the dates between which
    the momentum shall be calculated. A new :class:`list` containing only the
    values in the right time frame is built and passed to
    :py:func:`cumulative.momentum`.

    Returns the momentum of the security (:class:`float`)
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

    Moentum is computed as follow:
        - momentum = 100*(new - old)/old

    Returns the momentum of the vector (:class:`float`)
    """
    return 100*((vector[0] - vector[-1])/vector[-1])
