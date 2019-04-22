# -*- coding: UTF-8 -*-
import gbl, api
from db import db

def validate(raw):
    tickers = []
    raw = raw.replace(' ', '')                  # remove spaces
    raw = raw.replace('\n', '')                 # removes cr
    for item in raw.split(','):                 # comma split
        if item is not '':
            tickers.append(str(item).upper())
    return tickers

def save(ticks):
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
    db.portfolio.insert(name = name,
                        vol = vol,
                        cmr = cmr,
                        )

if __name__ == '__main__':
    save(['GOOGL', 'APPL', 'TSLA'])
    print(gbl.NAMES)
