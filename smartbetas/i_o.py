# -*- coding: UTF-8 -*-
""":mod:`__i_o__` is handle inputs and outputs generated from the console by
the user.
"""
from db import db

def portfolio(vol, cmr, cmp, prices):
    """ Displays a computed portfolio.

    .. code-block:: bash

        ----------------------------------------------------------------------
        | Pos |     Volatility     |      Momentum      |     Composite      |
        ----------------------------------------------------------------------
        |  1  |   AAPL     21.98   |   AAPL     5.88 %  |   AAPL    204.3 $  |
        |  2  |   TSLA     29.98   |   TSLA     0.3 %   |   TSLA    235.14 $ |
        ----------------------------------------------------------------------

    Returns nothing.
    """
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

def portfolios(p_flo):
    """ Displays a table listing all the saved portfolios.

    .. code-block:: bash

        ----------------------------------------------------------------------
        |  id |   Date   |      Name     |              Tickers              |
        ----------------------------------------------------------------------
        |  1  |2019-04-23|   Apple Test  |                AAPL               |
        |  2  |2019-04-23|   Test Apple  |                AAPL               |
        |  3  |2019-04-23|      Test     |                AAPL               |
        |  4  |2019-04-23| 14 Tickers ftw|      AMD, ACB, GWW, GOOGL...      |
        |  5  |2019-04-27|   Apple Only  |                AAPL               |
        |  6  |2019-04-27|  Apple Tesla  |           AAPL, TSLA...           |
        ----------------------------------------------------------------------

    Returns nothing.
    """
    counter = 1
    print('%s' % ('-'.center(70, '-')))
    print('|%5s|%10s|%15s|%35s|' % ('id'.center(5),
                                    'Date'.center(10),
                                    'Name'.center(15),
                                    'Tickers'.center(35)))
    print('%s' % ('-'.center(70, '-')))
    tickers = ''
    for row in p_flo:
        tickers = ', '.join(list(row['prc'].keys())[0:4])
        tickers += '...' if len(tickers)>4 else ''
        print('|%5s|%10s|%15s|%35s|' % (
                                        str(row['id']).center(5),
                                        str(row['date'])[:10].center(10),
                                        row['name'].center(15),
                                        str(tickers).center(35)))
        counter += 1
    print('%s' % ('-'.center(70, '-')))

def investment(qty):
    """ Prompts instructions to guide a user to invest 100'000 USD into a
    portfolio.

    .. code-block:: bash

        (beta): invest
         Invest 100'000 USD in each portefolio (y/n): y
         Invest in the [x] top securities (1): 1
         Name of the investment : Glorious Investment

    Returns nothing.
    """
    if input(" Invest 100'000 USD in each portefolio (y/n): ") == 'y':
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
    """ Displays a table listing all the investments made by the user.

    .. code-block:: bash

        ----------------------------------------------------------------------
        | Pos |    Id    |           Date          |           Name          |
        ----------------------------------------------------------------------
        |  1  |    1     |   2019-04-22 16:57:42   |       6 Big Stuffs      |
        |  2  |    2     |   2019-04-27 13:59:42   |           Test          |
        |  3  |    3     |   2019-04-27 14:05:07   |         One One         |
        |  4  |    4     |   2019-04-28 12:31:58   |   Glorious Investment   |
        |  5  |    5     |   2019-04-28 12:32:38   |   Glorious Investment   |
        ----------------------------------------------------------------------

    Returns nothing.
    """
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
    """ Displays a report with the returns for each portfolio.

    .. code-block:: bash

        --------------------------------------------------------------------------------
                                        One One - Report
        --------------------------------------------------------------------------------
                                   Volatility Based Portfolio
        --------------------------------------------------------------------------------
        | Ticker |N Shares| Purchase Date |  Initial  |  Current  | Abs Change|Returns |
        --------------------------------------------------------------------------------
        |  MBRX  | 12270  |   2019-04-27  |   1.63 $  |   1.42 $  | -2576.7 $ |-12.88 %|
        |  RAD   |  1992  |   2019-04-27  | 10.0401 $ |   9.08 $  | -1912.52 $|-9.56 % |
        |  KEYW  |  1784  |   2019-04-27  |  11.21 $  |   11.3 $  |  160.56 $ | 0.8 %  |
        |  ACB   |  2212  |   2019-04-27  |  9.0396 $ |   9.04 $  |   0.88 $  | 0.0 %  |
        |  STLD  |  609   |   2019-04-27  |  32.86 $  |  31.58 $  | -779.52 $ | -3.9 % |
        | Total  |   NA   |   2019-04-27  | 100006.0 $| 94898.7 $ | -5107.3 $ |-5.11 % |
        --------------------------------------------------------------------------------
                                    Momentum Based Portfolio
        --------------------------------------------------------------------------------
        | Ticker |N Shares| Purchase Date |  Initial  |  Current  | Abs Change|Returns |
        --------------------------------------------------------------------------------
        |  AMD   |  717   |   2019-04-27  |  27.89 $  |  27.88 $  |  -7.17 $  |-0.04 % |
        |  ACB   |  2212  |   2019-04-27  |  9.0396 $ |   9.04 $  |   0.88 $  | 0.0 %  |
        |  GWW   |   69   |   2019-04-27  | 291.015 $ |  291.91 $ |  61.76 $  | 0.31 % |
        | GOOGL  |   16   |   2019-04-27  | 1264.28 $ | 1277.42 $ |  210.24 $ | 1.04 % |
        |  BABA  |  107   |   2019-04-27  | 186.7425 $|  187.09 $ |  37.18 $  | 0.19 % |
        | Total  |   NA   |   2019-04-27  | 100282.7 $| 100585.6 $|  302.9 $  | 0.3 %  |
        --------------------------------------------------------------------------------
                                   Composite Based Portfolio
        --------------------------------------------------------------------------------
        | Ticker |N Shares| Purchase Date |  Initial  |  Current  | Abs Change|Returns |
        --------------------------------------------------------------------------------
        |  ACB   |  2212  |   2019-04-27  |  9.0396 $ |   9.04 $  |   0.88 $  | 0.0 %  |
        |  AMD   |  717   |   2019-04-27  |  27.89 $  |  27.88 $  |  -7.17 $  |-0.04 % |
        |  MBRX  | 12270  |   2019-04-27  |   1.63 $  |   1.42 $  | -2576.7 $ |-12.88 %|
        |  KEYW  |  1784  |   2019-04-27  |  11.21 $  |   11.3 $  |  160.56 $ | 0.8 %  |
        |  BABA  |  107   |   2019-04-27  | 186.7425 $|  187.09 $ |  37.18 $  | 0.19 % |
        | Total  |   NA   |   2019-04-27  | 99972.9 $ | 97587.7 $ | -2385.2 $ |-2.39 % |
        --------------------------------------------------------------------------------

    Returns nothing.
    """
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
    """ Displays a listing all the previously saved reports.

    .. code-block:: bash

        ----------------------------------------------------------------------
        | Pos |    Id    |           Date          |           Name          |
        ----------------------------------------------------------------------
        |  1  |    1     |        2019-04-26       |       6 Big Stuffs      |
        |  2  |    2     |        2019-04-27       |       6 Big Stuffs      |
        |  3  |    3     |        2019-04-27       |           Test          |
        |  4  |    4     |        2019-04-27       |       6 Big Stuffs      |
        |  5  |    5     |        2019-04-28       |         One One         |
        ----------------------------------------------------------------------

    Returns nothing.
    """
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

def tickers(row):
    """ Lists all the tickers and names saved in the database.

    .. code-block:: bash

        (beta): symbols
        -->   0: AAPL -  Apple Inc.
        -->   1: TSLA -  Tesla Inc.
        -->   2: GOOGL -  Alphabet Inc.
        -->   3: BABA -  Alibaba Group Holding Limited
        -->   4: GWW -  W.W. Grainger Inc.
        -->   5: CVX -  Chevron Corporation
        -->   6: HAL -  Bank Nova Scotia Halifax Pfd 3
        -->   7: RAD -  Credit Suisse X-Links Monthly Pay 2xLeveraged Alerian MLP Index Exchange Traded Notes due May 16 2036
        -->   8: MBRX -  Moleculin Biotech Inc.
        -->   9: KEYW -  The KEYW Holding Corporation
        -->  10: BBBY -  Bed Bath & Beyond Inc.
        -->  11: AMD -  Advanced Micro Devices Inc.
        -->  12: STLD -  Steel Dynamics Inc.
        -->  13: ACB -  Aurora Cannabis Inc.
        -->  14: ATHEN -  Athene Holding Ltd. Class A

    Returns nothing.
    """
    counter = 1
    print('%s' % ('-'.center(70, '-')))
    print('|%5s|%20s|%20s|%20s|' % ('id'.center(5),
                                    'vol'.center(20),
                                    'mom'.center(20),
                                    'comp'.center(20)))
    print('%s' % ('-'.center(70, '-')))
    for v, r, p in zip(row['vol'].keys(), row['cmr'].keys(), row['cmp'].keys()):
        print('|%5s|%20s|%20s|%20s|' % (
                                        str(counter).center(5),
                                        v.center(20),
                                        r.center(20),
                                        p.center(20)))
        v_name = db(db.symbols.ticker==v).select().as_list()[0]['name'][:18]
        r_name = db(db.symbols.ticker==r).select().as_list()[0]['name'][:18]
        p_name = db(db.symbols.ticker==p).select().as_list()[0]['name'][:18]
        print('|%5s|%20s|%20s|%20s|' % (
                                        str('').center(5),
                                        v_name.center(20),
                                        r_name.center(20),
                                        p_name.center(20)))
        counter += 1

    print('%s' % ('-'.center(70, '-')))
