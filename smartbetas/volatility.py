# -*- coding: UTF-8 -*-
from statistics import stdev
from datetime import datetime, timedelta

def volatility(data):
    # select only last two years
    vector = []
    today = datetime.today()
    delta = timedelta(weeks = 104)
    two_y = today - delta               # date two years ago

    for item in data:
        if item[0] >= two_y:
            vector.append(item[1])
    return stdev(vector)
