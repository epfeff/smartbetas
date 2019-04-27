import unittest
import volatility
import datetime

class TestVolatility(unittest.TestCase):
    def test_volatility(self):
        self.assertEqual(volatility.volatility(b), 5.489736255742988)

b = [[datetime.datetime(2019, 4, 22, 0, 0), 204.0899],
    [datetime.datetime(2019, 4, 18, 0, 0), 203.86],
    [datetime.datetime(2019, 4, 17, 0, 0), 203.13],
    [datetime.datetime(2019, 4, 16, 0, 0), 199.25],
    [datetime.datetime(2019, 4, 15, 0, 0), 199.23],
    [datetime.datetime(2019, 4, 12, 0, 0), 198.87],
    [datetime.datetime(2019, 4, 11, 0, 0), 198.95],
    [datetime.datetime(2019, 4, 10, 0, 0), 200.62],
    [datetime.datetime(2019, 4, 9, 0, 0), 199.5],
    [datetime.datetime(2019, 4, 8, 0, 0), 200.1],
    [datetime.datetime(2019, 4, 5, 0, 0), 197.0],
    [datetime.datetime(2019, 4, 4, 0, 0), 195.69],
    [datetime.datetime(2019, 4, 3, 0, 0), 195.35],
    [datetime.datetime(2019, 4, 2, 0, 0), 194.02],
    [datetime.datetime(2019, 4, 1, 0, 0), 191.24],
    [datetime.datetime(2019, 3, 29, 0, 0), 189.95],
    [datetime.datetime(2019, 3, 28, 0, 0), 188.72],
    [datetime.datetime(2019, 3, 27, 0, 0), 188.47],
    [datetime.datetime(2019, 3, 26, 0, 0), 186.79],
    [datetime.datetime(2019, 3, 25, 0, 0), 188.74],
    [datetime.datetime(2019, 3, 22, 0, 0), 191.05]]

if __name__ == '__main__':
    unittest.main()
