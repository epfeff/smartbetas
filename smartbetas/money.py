# -*- coding: UTF-8 -*-
from db import db
from datetime import datetime, date, timedelta

def invest(p_size, p_vol, p_cmr, p_cmp, prices, s_name, stack=100000):
    inv_vol = {}                    # investment on volatility portfolio
    inv_cmr = {}                    # investment on cumulative return portfolio
    inv_cmp = {}                    # investment on composite portfolio
    sec_inv = stack / p_size
    for i, j in enumerate(p_vol.keys()):
        if i < p_size:
            inv_vol[j] = round(sec_inv/prices[j])
    for i, j in enumerate(p_cmr.keys()):
        if i < p_size:
            inv_cmr[j] = round(sec_inv/prices[j])
    for i, j in enumerate(p_cmp.keys()):
        if i < p_size:
            inv_cmp[j] = round(sec_inv/prices[j])

    db.investments.insert(  date = datetime.now(),
                            name = s_name,
                            vol = inv_vol,
                            cmr = inv_cmr,
                            cmp = inv_cmp)
    db.commit()
