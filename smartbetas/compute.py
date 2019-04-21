# -*- coding: UTF-8 -*-
import api, json, volatility, cumulative, composite, i_o, gbl, time
from datetime import datetime, date, timedelta

def smartbetas(tickers):
    start = time.time()
    v_vol = []                      # volatility vector
    v_cmr = []                      # cumulative return vector
    p_vol = {}                      # portfolio volatility
    p_cmr = {}                      # portfolio cumulative return
    p_cmp = {}                      # portfolio composite
    prices = {}                     # stores the prices
    p_size = 0                      # investment portfolio quantity of tickers

    for tick in tickers:
        data = api.tsd(tick)
        prices[tick] = data[0][1]
        v_vol.append((tick, volatility.volatility(data)))
        v_cmr.append((tick, cumulative.cumulative(data)))

    # sorting the vectors
    v_vol.sort(key = lambda x: x[1])
    v_cmr.sort(key = lambda x: x[1], reverse = True)
    # vectors to dict
    for vol, cmr in zip(v_vol, v_cmr):
        p_vol[vol[0]] = vol[1]
        p_cmr[cmr[0]] = cmr[1]
    # composite vector
    p_cmp = composite.composite(p_vol, p_cmr)
    # display table of outputs
    i_o.portfolio(p_vol, p_cmr, p_cmp, prices)
    # saves in global var
    gbl.P_VOL = p_vol
    gbl.P_CMR = p_cmr
    gbl.P_CMP = p_cmp
    gbl.PRICES = prices
    print(time.time()-start)

if __name__ == '__main__':
    smartbetas(['APPL', 'GOOGL', 'SBUX', 'TSLA', 'AMZN'])
