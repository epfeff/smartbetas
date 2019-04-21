# -*- coding: UTF-8 -*-
import cmd, os, tickers, gbl, api
from db import db

class betacmd(cmd.Cmd):
    intro = 'Smart Betas strategy calculator - Requires an internet connection'
    prompt = '(beta): '
    out = '-->'
    file = None

    def do_load(self, arg):
        # Checks if the specified file exists
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
        print('%s %s tickers stored' % (self.out, len(gbl.TICKERS)))
        for i, tick in enumerate(gbl.TICKERS):
            print('%s %3s: %s -  %s' % (self.out, i, tick, gbl.NAMES[i]))

    def do_symbols(self, arg):
        symbols = db(db.symbols).select()
        if len(symbols) == 0:
            print('%s %s' % (self.out, 'no symbols stored'))
            return
        for i, sym in enumerate(symbols):
            print('%s %3s: %s -  %s' % (self.out, i, sym.ticker, sym.name))

    def do_compute(self, arg):
        print('compute')
        print(arg)

    def do_save(self, arg):
        print('save')

    def do_bye(self, arg):
        print('terminating...')
        exit()
