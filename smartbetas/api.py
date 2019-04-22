# -*- coding: UTF-8 -*-
import urllib.request, json, datetime, time
from datetime import datetime

def symbol(tick):
    sym = urllib.request.urlopen('https://ticker-2e1ica8b9.now.sh/keyword/%s' % tick)
    data = json.load(sym)
    if len(data) > 0:
        return data[0]['name']
    else:
        return None

def tsd(tick):
    # json key holding the data
    daily = 'Time Series (Daily)'
    error = 'Error Message'
    close = []
    out = '(-api):'
    # file = '%s.json' % tick
    # insert code to get data from API
    #data =  json.loads(open(file, 'r').read())
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=K44NPIPA1JQK6QGM" % (tick)
    print('%s fetching data for %s' %(out, tick))
    raw = urllib.request.urlopen(url)
    print('%s data fetched for %s!' % (out,tick))
    data = json.load(raw)

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


if __name__ == '__main__':
    tsm('lol')
