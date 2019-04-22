# -*- coding: UTF-8 -*-
try:
    import pydal
except ImportError:
    print("pydal module is missing")
    exit()
# imports modules
from console import betacmd
import db, os
# clears the console
os.system('cls') if os.name == 'nt' else os.system('clear')
# starts the program
if __name__ == '__main__':
    betacmd().cmdloop()
