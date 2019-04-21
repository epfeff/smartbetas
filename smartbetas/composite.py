# -*- coding: UTF-8 -*-

def composite(vol, cmr):
    vector = {}
    v_sort = []
    composite = {}
    for item in vol.keys():
        vector[item] = 0
    for i, j in enumerate(vol.keys()): vector[j] += i
    for i, j in enumerate(cmr.keys()): vector[j] += i

    # translates to tuple to sort
    for item in vector.keys():
        v_sort.append((item, vector[item]))
    v_sort.sort(key = lambda x: x[1])

    # back to dict
    for item in v_sort:
        composite[item[0]] = item[1]

    return composite
