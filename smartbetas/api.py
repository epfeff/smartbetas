# -*- coding: UTF-8 -*-
import urllib.request, json
#test
def symbol(tick):
    sym = urllib.request.urlopen('https://ticker-2e1ica8b9.now.sh/keyword/%s' % tick)
    data = json.load(sym)
    if len(data) > 0:
        return data[0]['name']
    else:
        return None

def tsm(tick):
    close = []
    # insert real code one day
    data =  json.loads(open('tsm.json', 'r').read())
    # rearrange data for convinience
    for item in data['Monthly Time Series']:
        monthly = {item : data['Monthly Time Series'][item]['4. close'] }
        close.append(monthly)
    return close


if __name__ == '__main__':
    tsm('lol')
