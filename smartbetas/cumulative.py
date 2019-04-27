# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta

def ret(data):
    vector = []
    today = datetime.today()
    delta1 = timedelta(weeks = 8)
    delta2 = timedelta(weeks = 52)
    two_m = today - delta1
    one_y = today - delta2

    for item in data:
        if item[0] <= two_m and item[0] >= one_y:
            vector.append(item[1])

    cmr = momentum(vector)
    return cmr

def momentum(vector):
    return 100*((vector[0] - vector[-1])/vector[-1])
