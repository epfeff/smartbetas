Welcome to SmartBetas's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


SmartBetas Investing
--------------------
:mod:`__main__` is initiating the application and starting the console.

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

Database Layer
--------------
.. automodule :: db

Tickers Management
------------------
.. automodule :: tickers
   :members:

API Management
--------------
.. automodule :: api
   :members:

Computing results
-----------------
.. automodule :: compute
   :members:

Volatility
**********
.. automodule :: volatility
   :members:

Momentum
********
.. automodule :: cumulative
   :members:

Composite
*********
.. automodule :: composite
   :members:

Investing
---------
.. automodule :: money
   :members:

User Interface
--------------
.. automodule :: console
   :members:

Checking Out Results
--------------------
.. automodule :: check
   :members:

Input / Outputs
---------------
.. automodule :: i_o
   :members:

Global Variables
----------------
.. automodule :: gbl
   :members:

Test Modules
----------------
.. automodule :: test_volatility
   :members:
.. automodule :: test_cumulative
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
