# -*- coding: UTF-8 -*-

def portfolio(vol, cmr, cmp, prices):
    counter = 1
    print('%s' % ('-'.center(70, '-')))
    print('|%5s|%20s|%20s|%20s|' % ('Pos'.center(5),
                                    'Volatility'.center(20),
                                    'Cumulative'.center(20),
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
                                        (str(prices[p])+' $').center(10)))
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
