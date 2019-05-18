# -*- coding: UTF-8 -*-
""":mod:`api.py` handles communications between the host and the web APIs.
"""
import gbl
import urllib.request, json, datetime, time
from datetime import datetime

def symbol(tick):
    """ Determines the name of a stock based on a ticker.

    Parameters:
        - `tick` : :class:`string`  stock's ticker.

    Constructs the request URL with the ticker passed as argument then makes an
    `http` request and parses the data received from the API.

    `Json` Data sample from the API: ``[{"symbol":"AAPL","name":"Apple Inc."}]``

    Returns a :class:`string` contraining the name of the sock OR ``None``
    if the API failed to return data for the ticker (as example, if a wrong
    ticker was provided).
    """
    out = '(-api):'
    url = 'https://ticker-2e1ica8b9.now.sh/keyword/%s' % tick
    print('%s fetching data for %s' %(out, tick))
    sym = urllib.request.urlopen(url)
    data = json.load(sym)
    if len(data) > 0:
        return data[0]['name']
    else:
        return None

def tsd(tick):
    """ Fetches a stock daily data from 20 years ago till now.

    Parameters:
        - `tick` : :class:`string`  security ticker.

    The function builds the URL, makes the `http` request to the web API and
    parses the received JSON, then to assert that data was indeed returned,
    it checks the length of the data:

        - length = 2 : Data returned
        - length < 2 : No data returned

    If no data is returned, the function assumes that the maximum amount of
    calls per minute is reached; it will wait for 15 seconds and retry; if it
    fails again it will wait again till data is returned.

    .. note::
      If the maximum amount of daily request is reached, the function will loop
      forever.

    Data sample:

    .. code-block:: json

        {
        "Meta Data": {
            "1. Information": "Daily Prices (open, high, low, close) Volumes",
            "2. Symbol": "AAPL",
            "3. Last Refreshed": "2019-04-26",
            "4. Output Size": "Full size",
            "5. Time Zone": "US/Eastern"
        },
        "Time Series (Daily)": {
            "2019-04-26": {
                "1. open": "204.9000",
                "2. high": "205.0000",
                "3. low": "202.1200",
                "4. close": "204.3000",
                "5. volume": "18611948"
            },  // max 20 years of values
            ...

    Once the data was obtained, the function will create a :class:`list` of
    :class:`tuple` containing in each position a datetime object and the closing
    price of the stock for that date. (List starts with the date closest to now)

    List sample : ``[(datetime.datetime(2019, 4, 18, 0, 0), 203.86)]``

    Returns a :class:`list` of :class:`tuple` containing dates and closing
    prices.
    """
    # json key holding the data
    daily = 'Time Series (Daily)'
    error = 'Error Message'
    close = []
    out = '(-api):'
    url = gbl.API_URL % (tick, gbl.API_KEY)
    print('%s fetching data for %s' %(out, tick))
    raw = urllib.request.urlopen(url)
    print('%s data fetched for %s!' % (out,tick))
    data = json.load(raw)
    # API overusage handling
    if len(data) < 2:
        if error not in list(data.keys()):
            print('%s Reached max request per minutes - waiting...' % (out))
            while len(data) < 2:
                time.sleep(15)
                print('%s trying %s again' %(out, tick))
                raw = urllib.request.urlopen(url)
                print('%s data fetched for %s!' % (out, tick))
                data = json.load(raw)
                print('%s too early...' % (out) ) if len(data) <2 else print('%s %s ok' % (out, tick))
    # rearrange data, sets strings date to datetime objects
    for item in data[daily]:
        date = datetime.strptime(item, '%Y-%m-%d')
        monthly = [date, float(data[daily][item]['4. close'])]
        close.append(monthly)
    return close
