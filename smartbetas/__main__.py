# -*- coding: UTF-8 -*-
""":mod:`main.py` is initiating the application
"""
try:
    import pydal
except ImportError:
    print("Error: pydal module is missing")
    exit()
# imports modules
from console import betacmd
import db, os, socket
# clears the console
os.system('cls') if os.name == 'nt' else os.system('clear')
# checks if the host can reach internet
try:
    socket.create_connection(("www.google.com", 80))
except OSError:
    print('Error: not connected to internet !')
    exit()
# starts the program
betacmd().cmdloop()
