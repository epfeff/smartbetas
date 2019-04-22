# -*- coding: UTF-8 -*-
from db import db

def portfolio(vol, cmr, cmp, prices):
    counter = 1
    print('%s' % ('-'.center(70, '-')))
    print('|%5s|%20s|%20s|%20s|' % ('Pos'.center(5),
                                    'Volatility'.center(20),
                                    'Momentum'.center(20),
                                    'Composite'.center(20)))
    print('%s' % ('-'.center(70, '-')))
    for v, r, p in zip(vol.keys(), cmr.keys(), cmp.keys()):
        print('|%5s|%10s%10s|%10s%10s|%10s%10s|' % (
                                        str(counter).center(5),
                                        v.center(10),
                                        str(round(vol[v],2)).center(10),
                                        r.center(10),
                                        (str(round(cmr[r],2))+' %').center(10),
                                        p.center(10),
                                        (str(round(prices[p],2))+' $').center(10)))
        counter +=1
    print('%s' % ('-'.center(70, '-')))

def investment(qty):
    if input(' Invest 100000K in each portefolio (y/n): ') == 'y':
        p_size = s_name = ''
        while (p_size.isdigit() == False):
            p_size = input(' Invest in the [x] top securities (%s): ' % (qty))
        p_size = int(p_size)
        while (s_name == ''):
            s_name = input(' Name of the investment : ')
        return p_size, s_name
    else:
        return False, False

def sessions(inv):
    counter = 1
    print('%s' % ('-'.center(70, '-')))
    print('|%5s|%10s|%25s|%25s|' % ('Pos'.center(5),
                                    'Id'.center(10),
                                    'Date'.center(25),
                                    'Name'.center(25)))
    print('%s' % ('-'.center(70, '-')))
    for row in inv:
        print('|%5s|%10s|%25s|%25s|' % (
                                        str(counter).center(5),
                                        str(row.id).center(10),
                                        str(row.date).center(25),
                                        row.name.center(25)))
        counter +=1
    print('%s' % ('-'.center(70, '-')))

def returns(vol, cmr, cmp, name):
    print('%s' % ('-'.center(80, '-')))
    print(('%s - Report' %(name)).center(80))
    print('%s' % ('-'.center(80, '-')))
    print('%s' % ('Volatility Based Portfolio'.center(80, ' ')))
    print('%s' % ('-'.center(80, '-')))
    print('|%8s|%8s|%15s|%11s|%11s|%11s|%8s|' % ('Ticker'.center(8),
                                        'N Shares'.center(8),
                                        'Purchase Date'.center(15),
                                        'Initial'.center(11),
                                        'Current'.center(11),
                                        'Abs Change'.center(11),
                                        'Returns'.center(8)))
    print('%s' % ('-'.center(80, '-')))
    for t in vol:
        print('|%8s|%8s|%15s|%11s|%11s|%11s|%8s|' % (t.center(8),
                                        str(vol[t]['qty']).center(8),
                                        str(vol[t]['date'])[:10].center(15),
                                        (str(vol[t]['old'])+' $').center(11),
                                        (str(vol[t]['new'])+' $').center(11),
                                        (str(vol[t]['abs'])+' $').center(11),
                                        (str(vol[t]['rel'])+' %').center(8)))
    print('%s' % ('-'.center(80, '-')))
    print('%s' % ('Momentum Based Portfolio'.center(80, ' ')))
    print('%s' % ('-'.center(80, '-')))
    print('|%8s|%8s|%15s|%11s|%11s|%11s|%8s|' % ('Ticker'.center(8),
                                        'N Shares'.center(8),
                                        'Purchase Date'.center(15),
                                        'Initial'.center(11),
                                        'Current'.center(11),
                                        'Abs Change'.center(11),
                                        'Returns'.center(8)))
    print('%s' % ('-'.center(80, '-')))
    for t in cmr:
        print('|%8s|%8s|%15s|%11s|%11s|%11s|%8s|' % (t.center(8),
                                        str(cmr[t]['qty']).center(8),
                                        str(cmr[t]['date'])[:10].center(15),
                                        (str(cmr[t]['old'])+' $').center(11),
                                        (str(cmr[t]['new'])+' $').center(11),
                                        (str(cmr[t]['abs'])+' $').center(11),
                                        (str(cmr[t]['rel'])+' %').center(8)))
    print('%s' % ('-'.center(80, '-')))
    print('%s' % ('Composite Based Portfolio'.center(80, ' ')))
    print('%s' % ('-'.center(80, '-')))
    print('|%8s|%8s|%15s|%11s|%11s|%11s|%8s|' % ('Ticker'.center(8),
                                        'N Shares'.center(8),
                                        'Purchase Date'.center(15),
                                        'Initial'.center(11),
                                        'Current'.center(11),
                                        'Abs Change'.center(11),
                                        'Returns'.center(8)))
    print('%s' % ('-'.center(80, '-')))
    for t in cmp:
        print('|%8s|%8s|%15s|%11s|%11s|%11s|%8s|' % (t.center(8),
                                        str(cmp[t]['qty']).center(8),
                                        str(cmp[t]['date'])[:10].center(15),
                                        (str(cmp[t]['old'])+' $').center(11),
                                        (str(cmp[t]['new'])+' $').center(11),
                                        (str(cmp[t]['abs'])+' $').center(11),
                                        (str(cmp[t]['rel'])+' %').center(8)))
    print('%s' % ('-'.center(80, '-')))

def reports(rep):
    counter = 1
    print('%s' % ('-'.center(70, '-')))
    print('|%5s|%10s|%25s|%25s|' % ('Pos'.center(5),
                                    'Id'.center(10),
                                    'Date'.center(25),
                                    'Name'.center(25)))
    print('%s' % ('-'.center(70, '-')))
    for row in rep:
        print('|%5s|%10s|%25s|%25s|' % (
                                        str(counter).center(5),
                                        str(row.id).center(10),
                                        str(row.date).center(25),
                                        row.name.center(25)))
        counter +=1
    print('%s' % ('-'.center(70, '-')))
