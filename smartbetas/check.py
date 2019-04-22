# -*- coding: UTF-8 -*-
import api
import concurrent.futures
from db import db
from datetime import datetime

def sessions(id):
    r_vol = {}                      # returns on the volability portfolio
    r_cmr = {}                      # returns on the cumulative return pf
    r_cmp = {}                      # returns on the composite portfolio

    n_prices = []                   # return of the paralel processing

    inv = db(db.investments.id == id).select().as_list()[0]

    tickers = list(inv['prc'].keys())

    with concurrent.futures.ProcessPoolExecutor() as executor:
        n_prices = list(executor.map(compute, tickers))

    n_prices = {x[0]:x[1] for x in n_prices}

    r_vol = returns(inv, 'vol', n_prices)
    r_cmr = returns(inv, 'cmr', n_prices)
    r_cmp = returns(inv, 'cmp', n_prices)

    db.checks.insert(       date = str(datetime.now())[:10],
                            name = inv['name'],
                            vol = r_vol,
                            cmr = r_cmr,
                            cmp = r_cmp)
    db.commit()

    return r_vol, r_cmr, r_cmp, inv['name']

def compute(tick):
    data = api.tsd(tick)
    price = (tick, data[0][1])
    return price

def returns(inv, pfl, prices):
    out = dict()
    for t in list(inv[pfl].keys()):
        new = prices[t]
        old = inv['prc'][t]
        qty = inv[pfl][t]
        date = inv['date']
        out[t] = dict()
        out[t]['old'] = old
        out[t]['new'] = new
        out[t]['abs'] = round((qty *new) - (qty * old), 2)
        out[t]['rel'] = round((((new - old) / old) * 100), 2)
        out[t]['qty'] = qty
        out[t]['date'] = date
    out['Total'] = t_returns(inv, pfl, prices, date)
    return out

def t_returns(inv, pfl, prices, date):
    t_old = sum(map(lambda key: inv[pfl][key]*inv['prc'][key], inv[pfl].keys()))
    t_old = round(t_old, 1)
    t_new = sum(map(lambda key: inv[pfl][key]*prices[key], inv[pfl].keys()))
    t_new = round(t_new, 1)
    abs = round(t_new - t_old, 1)
    rel = round(((t_new - t_old) / t_old) * 100, 2)
    return {'abs': abs, 'rel': rel, 'old': t_old,
        'new': t_new, 'qty': 'NA', 'date': date}


if __name__ == '__main__':
    sessions(24)
