# -*- coding: UTF-8 -*-
import cmd, os, tickers, gbl, api, compute, i_o, money, check
from db import db

class betacmd(cmd.Cmd):
    intro = 'Smart Betas Investing - Requires an internet connection'
    prompt = '(beta): '
    out = '-->'
    file = None

    # empy lines do nothing
    def emptyline(self):
        return

    def do_load(self, arg):
        """ Loads a file containing tickers

        usage: load <FILENAME>

        Tickers in the file should be coma separated.
        """
        # Checks if the specified file exists
        gbl.TICKERS = []
        if os.path.isfile(arg):
            print('%s found %s!' % (self.out, arg))
            ticks = tickers.validate(open(arg, 'r').read())
            print('%s found %s tickers' % (self.out, len(ticks)))
            for i, tick in enumerate(ticks):
                print('%s %3s: %s ' % (self.out, i, tick))
            if input('%s save tickers ? (y/n): ' %(self.out)) == 'y':
                wr = tickers.save(ticks)
                if len(wr) > 0:
                    for item in wr:
                        print("%s ERROR: '%s' not found!" %(self.out, item))
                print('%s tickers list saved !' % (self.out))
        else:
            print("%s '%s' not found" % (self.out, arg))

    def do_show(self, arg):
        """ Displays tickers ready for computing.

        usage: show
        """
        print('%s %s ticker(s) ready' % (self.out, len(gbl.TICKERS)))
        for i, tick in enumerate(gbl.TICKERS):
            print('%s %3s: %s -  %s' % (self.out, i, tick, gbl.NAMES[i]))

    def do_symbols(self, arg):
        """ Display tickers stored in the database

        usage: symbols
        """
        symbols = db(db.symbols).select()
        if len(symbols) == 0:
            print('%s %s' % (self.out, 'no symbols stored'))
            return
        for i, sym in enumerate(symbols):
            print('%s %3s: %s -  %s' % (self.out, i, sym.ticker, sym.name))

    def do_compute(self, arg):
        """ Computes tickers in the pipe into a portfolio

        usage: compute
        """
        if len(gbl.TICKERS) > 0:
            compute.smartbetas(gbl.TICKERS)
            if input('%s save portfolio (y/n)' % (self.out)) == 'y':
                name = input('%s portfolio name: ' % (self.out))
                tickers.save_portfolio(gbl.P_VOL, gbl.P_CMR, gbl.P_CMP, gbl.PRICES, name)
        else:
            print('%s load some tickers first (load filename)' % (self.out))

    def do_portfolio(self, arg):
        print('%s current portfolio' % (self.out))
        i_o.portfolio(gbl.P_VOL, gbl.P_CMR, gbl.P_CMP, gbl.PRICES)

    def do_invest(self, arg):
        p_size = 10 if len(gbl.P_VOL)>10 else len(gbl.P_VOL)
        s_name = ''
        p_size, s_name = i_o.investment(p_size)
        if p_size == False and s_name == False: return
        #invests some cash
        money.invest(p_size, gbl.P_VOL, gbl.P_CMR,
            gbl.P_CMP, gbl.PRICES, s_name, 100000)

    def do_check(self, arg):
        inv = db(db.investments).select(orderby=db.investments.date)
        r_id = [row.id for row in inv]
        i_o.sessions(inv)
        s_id = ''
        while True:
            try:
                s_id = int(input('%s Session ID ? (Id): ' %(self.out)))
                if s_id not in r_id:
                    raise ValueError
            except ValueError:
                print('%s enter a number within Id range !' %(self.out))
                continue
            else:
                break
        vol, cmr, cmp, name = check.sessions(s_id)
        i_o.returns(vol, cmr, cmp, name)

    def do_report(self, arg):
        rep = db(db.checks).select()
        r_id = [row.id for row in rep]
        i_o.reports(rep)
        s_id = ''
        while True:
            try:
                s_id = int(input('%s Report ID ? (Id): ' %(self.out)))
                if s_id not in r_id:
                    raise ValueError
            except ValueError:
                print('%s enter a number within Id range !' %(self.out))
                continue
            else:
                break
        rep = db(db.checks.id == s_id).select()[0]
        i_o.returns(rep['vol'], rep['cmr'], rep['cmp'], rep['name'])


    def do_bye(self, arg):
        print('terminating...')
        exit()
