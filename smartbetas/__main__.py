# -*- coding: UTF-8 -*-
""":mod:`__main__` is initiating the application and starting the console.

The module checks if the required library is installed on the host and if
the host is connected to the internet. If the tests succeed, it starts the
user interface console.

The program is built on a database, the communications between the program and
the db is managed by pydal (Python Database Abstraction Layer). :mod:`__main__`
checks if `pydal` is installed on the host; if not, the program outputs a
message and closes.

The module will also check if the host is connected to the internet, this is
required because the data used to compute portfolios is pulled from an API.
If the host is not connected to the internet the program will close.

The connectivity test is performed by trying to open a socket on google's TCP
port 80.

This module also clears the console of whatever was currently displayed on it
prior starting the console.

.. _pyDal's API documentation:
   https://pydal.readthedocs.io/en/latest/

.. _Python socket - Low-level netorking interface:
   https://docs.python.org/3/library/socket.html
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
if __name__ == '__main__':
    betacmd().cmdloop()
