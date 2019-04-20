# -*- coding: UTF-8 -*-
try:
    import pydal
except ImportError:
    print("pydal module is missing")
    exit()

from console import betacmd
import db

if __name__ == '__main__':
    betacmd().cmdloop()
