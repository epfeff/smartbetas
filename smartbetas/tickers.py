# -*- coding: UTF-8 -*-
"""
:mod:`tickers.py` is handles operations related to tickers.
"""
from datetime import datetime
import gbl, api
from db import db

def validate(raw):
    """ Checks the content of the data provided by the user.

    Users provide tickers to the application by writing them into a file
    that is loaded through the console interface with the <load filename>
    command.

    We expect the file to be filled with coma separated tickers :class:`string`.

    Parameters:
        - `raw` : :class:`string` content of the user provided file.

    The function strips the raw data from spaces, carrier returns and split the
    content around comas. It will also check if there are trailing comas or if
    the user mistakenly put two comas instead of one between tickers.

    Returns a :class:`list` of sanitized tickers
    """
    tickers = []
    raw = raw.replace(' ', '')                  # remove spaces
    raw = raw.replace('\n', '')                 # removes cr
    for item in raw.split(','):                 # comma split
        if item is not '':
            tickers.append(str(item).upper())
    return tickers

def save(ticks):
    """ Saves toclers names into a global variable and into the database.

    Parameters:
        - `ticks` : :class:`list` of :class:`string` , each one is a tickert.

    The function will check for each ticker if an entry already exists in the
    database, if not, it will attempt to fetch the ticker's name from a web API.

    If the fetch is successfull, the result is written into the database. This
    way next time the ticker is used, the application will not need to pull
    data from the web API.

    The function also sets the global `TICKERS` and `NAMES` :class:`list` with
    the tickers and their corresponding names.

    When a ticker can not be identified on the web API, it is not stored in the
    global variable nor in the database, but in a list that will be returned.

    Returns a :class:`list` containing tickers that caused errors.
    """
    errors = []
    # verifiy if the symbol is already present in the db
    # otherwise fetches it from the public api and inserts it into the DB
    for item in ticks:
        row = db(db.symbols.ticker == item).select()
        if len(row) == 0:
            name = api.symbol(item)
            if name != None:
                db.symbols.insert(ticker = item, name = name)
                db.commit()
                gbl.TICKERS.append(item)
                gbl.NAMES.append(name)
            else:
                errors.append(item)
        else:
            gbl.TICKERS.append(row[0].ticker)
            gbl.NAMES.append(row[0].name)
    return errors

def save_portfolio(vol, cmr, cmp, prices, name):
    """ Writes the computed portfolios into the database.

    Parameters:
        - `vol`  : :class:`dict` volatility portfolio.
        - `cmr`  : :class:`dict` momentum portfolio.
        - `cmp`  : :class:`dict` composite portfolio.
        - `prices` : :class:`dict` price register.
        - `name` : :class:`string` name of the portfolio.


    Saves into the database the items passed as argument.

    Returns `True` if it succeeded.
    """
    db.portfolios.insert(name = name,
                        vol = vol,
                        cmr = cmr,
                        cmp = cmp,
                        prc = prices,
                        date = datetime.now())
    db.commit()
    return True
