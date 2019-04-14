# -*- coding: UTF-8 -*-
import api, json
from db import db

def smartbetas(tickers):
    for tick in tickers:
        data = api.tsm(tick)
    for item in data:
        print(item)



if __name__ == '__main__':
    smartbetas(['APPL'])
