# -*- coding: UTF-8 -*-
import api, json,concurrent.futures
import volatility, cumulative, composite, i_o, gbl
from threading import Thread

def smartbetas(tickers):
    p_cmr = {}                      # portfolio cumulative return
    p_cmp = {}                      # portfolio composite
    v_r_p = []                      # volability, return and prices map

    # paralel processing of the computing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        v_r_p = list(executor.map(compute, tickers))
    # sorts into two dicts
    v_r_p.sort(key = lambda x: x[0][1])
    p_vol = {x[0][0]:x[0][1] for x in v_r_p}
    v_r_p.sort(key = lambda x: x[1][1], reverse = True)
    p_cmr = {x[1][0]:x[1][1] for x in v_r_p}
    prices = {x[2][0]:x[2][1] for x in v_r_p}
    # composite vector
    p_cmp = composite.composite(p_vol, p_cmr)
    # display table of outputs
    i_o.portfolio(p_vol, p_cmr, p_cmp, prices)

    gbl.P_VOL = p_vol
    gbl.P_CMR = p_cmr
    gbl.P_CMP = p_cmp
    gbl.PRICES = prices

def compute(tick):
    data = api.tsd(tick)
    price = (tick, data[0][1])
    vol = (tick, volatility.volatility(data))
    cmr = (tick, cumulative.ret(data))
    return [vol, cmr, price]

if __name__ == '__main__':
    smartbetas(['APPL', 'GOOGL', 'SBUX', 'TSLA', 'AMZN'])
