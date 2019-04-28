# -*- coding: UTF-8 -*-
""":mod:`__api__` handles communications between the host and the web APIs.

A web API is an Application Programming Interface for a web server or a web
browser. On the server side, it consists or one or more publicly exposed
endpoints accessible through `http` requests. The content is typically expressed
in JSON (JavaScript Object Notation) or XML (eXtensible Markup Language).

:mod:`__smartbetas__` relies on two APIs. One is used to convert tickers to
company names (As example: AAPL -> Apple Inc), the second one is used to get
information about a security (daily open, daily high, daily low, daily close and
daily volume).

The ticker API is totally free and open source, it is maintained by a single
contributor (`Kambala Yashwanth <https://github.com/yashwanth2804>`_), this API
simply takes a ticker as input and returns the name of the equity if found.

(`Alpha Vantage <https://www.alphavantage.co>`_) provides the stock data API.
This is not a free service, however they offer a free limited access to their
data. The following constraints are applicable when using a free account:

    - 5 API requests per minute
    - 500 API requests per day

Note that Alpha Vantage requires free users to register to get an API key. The
key is stored in :mod:`__gbl__`.

.. _Wikipedia Web API:
   https://en.wikipedia.org/wiki/Web_API

.. _Ticker Search API doc:
   https://github.com/yashwanth2804/TickerSymbol

.. _Alpha Vantage API Documentation:
   https://www.alphavantage.co/documentation/
"""
import gbl
import urllib.request, json, datetime, time
from datetime import datetime

def symbol(tick):
    """ Determines the name of a security based on a ticker.

    Parameters:
        - `tick` : :class:`string`  security ticker.

    Constructs the request URL with the ticker passed as argument then makes the
    request and parses the data received from the API.

    Data sample from the API: ``[{"symbol":"AAPL","name":"Apple Inc."}]``

    This function is always called before the software tries to obtain stock
    data about a security, therefore it filters wrong/bad tickers provided by
    the user.

    Returns a :class:`string` contraining the name of the security OR ``None``
    if the API failed to return data for the ticker.
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
    """ Fetches a security daily data from 20 years ago till now.

    Parameters:
        - `tick` : :class:`string`  security ticker.

    The function makes the API call and parses the JSON, then to assert that
    data was indeed returned, it checks the length of the data:
    - l=2 : Data returned
    - l<2 : No data returned

    If no data is returned, the function assumes that the maximum amount of
    calls per minute is reached; it will wait for 15 seconds and retry if it
    fails again it will wait again etc.. till data is returned.

    Note: The function can not handle the maximum amount of requests, if it is
    the case, it will loop forever.

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
            },
            ...

    Once the data was obtained, the function will create a :class:`list` of
    tuple containing in each position a datetime object and the closing price
    of the security. (List starts with the date closest to now)

    List sample : ``[(datetime.datetime(2019, 4, 18, 0, 0), 203.86)]``

    Returns a :class:`list` of :class:`tuple` with date and closing price.
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
