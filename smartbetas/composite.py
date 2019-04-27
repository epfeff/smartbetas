# -*- coding: UTF-8 -*-
""":mod:`__composite__` is used to determine a composite portfolio.

In this application we define a composite portfolio as a portfolio based on the
ranking of a security in the volatility portfolio and in the momentum portfolio.

The score of security is the sum of its index (position) in the two other
portfolio. The securities are then sorted in an ascending fasion.
"""

def composite(vol, cmr):
    """ Ranks securities in a composite fashion.

    Parameters:
        - `vol` : :class:`dict`  volatility portfolio.
        - `cmr` : :class:`dict`  momentum portfolio.

    Note: at this point, the two portfolios have the same tickers, only their
    ranking varies.

    The function builds a :class:`dict` with the tickers and set their score
    to zero; sample {'ticker': 0}. Then it adds to the ticker score their index
    in volatility and momentum portfolio.

    To rank the tickers, the :class:`dict` is transformed into a :class:`tuple`,
     sorted and transformed back into a :class:`dict`.

     Returns a :class:`dict` containing tickers and their score.

    """
    vector = {}                        # used to store tickers indexes
    v_sort = []                        # to store ranked tickers
    composite = {}                     # to store the return of the function
    # populates a dict with all the tickers and attributes them a score of 0
    for item in vol.keys():
        vector[item] = 0
    for i, j in enumerate(vol.keys()): vector[j] += i
    for i, j in enumerate(cmr.keys()): vector[j] += i
    # translates to tuple to sort
    for item in vector.keys():
        v_sort.append((item, vector[item]))
    v_sort.sort(key = lambda x: x[1])
    # back to dict
    for item in v_sort:
        composite[item[0]] = item[1]

    return composite
