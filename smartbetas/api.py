# -*- coding: UTF-8 -*-
import urllib.request, json, datetime
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
    close = []
    file = '%s.json' % tick
    # insert code to get data from API
    data =  json.loads(open(file, 'r').read())
    # rearrange data, sets strings date to datetime objects
    for item in data[daily]:
        date = datetime.strptime(item, '%Y-%m-%d')
        monthly = [date, float(data[daily][item]['4. close'])]
        close.append(monthly)
    return close


if __name__ == '__main__':
    tsm('lol')
