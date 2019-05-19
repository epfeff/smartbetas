## SmartBetas - Getting Started

Clone or download the repository on your computer:

```shell
git clone https://github.com/epfeff/smartbetas.git
```

Make sure that the required libraries are installed on your computer:
```shell
pip install pydal
```
Navigate to the root folder of the package and create a file containing stock tickers:
```shell
cd smartbetas
nano tickers.txt
....
```

Start the program and load the stock tickers file:
```shell
python smartbetas
....
Smart Betas Investing - Requires an internet connection
(beta):
....
(beta): load tickers.txt
--> found tickers.txt!
--> found 2 tickers
-->   0: AAPL
-->   1: TSLA
--> save tickers ? (y/n): y
```

You can confirm that the tickers were properly saved with `show tickers`:
```shell
(beta): show tickers
--> 2 ticker(s) ready
-->   0: AAPL -  Apple Inc.
-->   1: TSLA -  Tesla Inc.
```

You can then ask the program to generate a portfolio collection with `compute`:
```shell
(beta): compute
(-api): fetching data for AAPL
(-api): fetching data for TSLA
(-api): data fetched for TSLA!
(-api): data fetched for AAPL!
----------------------------------------------------------------------
| Pos |     Volatility     |      Momentum      |     Composite      |
----------------------------------------------------------------------
|  1  |   AAPL      21.9   |   AAPL     1.82 %  |   AAPL    189.0 $  |
|  2  |   TSLA     33.12   |   TSLA    -7.02 %  |   TSLA    211.03 $ |
----------------------------------------------------------------------
--> save portfolio (y/n): y
--> portfolio name: MyPortfolio
--> portfolio MyPortfolio saved
```

The last generated portfolio collection is saved in the persistence layer, you can verify what is stored with `show portfolio`:
```shell
(beta): show portfolio
--> current portfolio
----------------------------------------------------------------------
| Pos |     Volatility     |      Momentum      |     Composite      |
----------------------------------------------------------------------
|  1  |   AAPL      21.9   |   AAPL     1.82 %  |   AAPL    189.0 $  |
|  2  |   TSLA     33.12   |   TSLA    -7.02 %  |   TSLA    211.03 $ |
----------------------------------------------------------------------
```

Investing 100'000 USD in each portfolio is done with `invest`:
```shell
(beta): invest
 Invest 100'000 USD in each portefolio (y/n): y
 Invest in the [x] top securities (2): 2
 Name of the investment : MyInvestment
```

You can list all the investment made wiht `show invest`:
```shell
(beta): show invest
----------------------------------------------------------------------
| Pos |    Id    |           Date          |           Name          |
----------------------------------------------------------------------
|  1  |    1     |   2019-04-22 16:57:42   |       MyInvestment1     |
|  2  |    2     |   2019-04-27 13:59:42   |       MyInvestment2     |
|  3  |    3     |   2019-04-27 14:05:07   |       MyInvestment3     |
|  4  |    4     |   2019-04-28 12:31:58   |       MyInvestment4     |
|  5  |    5     |   2019-04-28 12:32:38   |       MyInvestment5     |
|  6  |    6     |   2019-05-19 16:41:09   |       MyInvestment6     |
----------------------------------------------------------------------
```

To measure the returns of an investment, simple type in `check`:
```shell
(beta): check
----------------------------------------------------------------------
| Pos |    Id    |           Date          |           Name          |
----------------------------------------------------------------------
|  1  |    1     |   2019-04-22 16:57:42   |       MyInvestment1     |
|  2  |    2     |   2019-04-27 13:59:42   |       MyInvestment2     |
|  3  |    3     |   2019-04-27 14:05:07   |       MyInvestment3     |
|  4  |    4     |   2019-04-28 12:31:58   |       MyInvestment4     |
|  5  |    5     |   2019-04-28 12:32:38   |       MyInvestment5     |
|  6  |    6     |   2019-05-19 16:41:09   |       MyInvestment6     |
----------------------------------------------------------------------
--> Session ID ? (Id): 1
(-api): working....
--------------------------------------------------------------------------------
                             MyInvestment1 - Report
--------------------------------------------------------------------------------
                           Volatility Based Portfolio
--------------------------------------------------------------------------------
| Ticker |N Shares| Purchase Date |  Initial  |  Current  | Abs Change|Returns |
--------------------------------------------------------------------------------
|  MBRX  | 11261  |   2019-04-22  |   1.48 $  |   1.16 $  | -3603.52 $|-21.62 %|
|  RAD   |  1718  |   2019-04-22  |  9.7006 $ |   9.13 $  | -980.29 $ |-5.88 % |
|  KEYW  |  1487  |   2019-04-22  |  11.21 $  |  11.22 $  |  14.87 $  | 0.09 % |
|  ACB   |  1832  |   2019-04-22  |   9.1 $   |   8.68 $  | -769.44 $ |-4.62 % |
|  STLD  |  500   |   2019-04-22  |  33.335 $ |  30.02 $  | -1657.5 $ |-9.94 % |
|  AMD   |  597   |   2019-04-22  | 27.9316 $ |   27.5 $  | -257.67 $ |-1.55 % |
| Total  |   NA   |   2019-04-22  | 100015.0 $| 92761.5 $ | -7253.5 $ |-7.25 % |
--------------------------------------------------------------------------------
                            Momentum Based Portfolio
--------------------------------------------------------------------------------
| Ticker |N Shares| Purchase Date |  Initial  |  Current  | Abs Change|Returns |
--------------------------------------------------------------------------------
|  AMD   |  597   |   2019-04-22  | 27.9316 $ |   27.5 $  | -257.67 $ |-1.55 % |
|  ACB   |  1832  |   2019-04-22  |   9.1 $   |   8.68 $  | -769.44 $ |-4.62 % |
|  GWW   |   56   |   2019-04-22  |  298.71 $ |  267.1 $  | -1770.16 $|-10.58 %|
| GOOGL  |   13   |   2019-04-22  | 1241.93 $ | 1168.78 $ | -950.95 $ |-5.89 % |
|  AAPL  |   82   |   2019-04-22  |  204.29 $ |  189.0 $  | -1253.78 $|-7.48 % |
|  BABA  |   90   |   2019-04-22  | 185.195 $ |  169.57 $ | -1406.25 $|-8.44 % |
| Total  |   NA   |   2019-04-22  | 99638.5 $ | 93230.3 $ | -6408.2 $ |-6.43 % |
--------------------------------------------------------------------------------
                           Composite Based Portfolio
--------------------------------------------------------------------------------
| Ticker |N Shares| Purchase Date |  Initial  |  Current  | Abs Change|Returns |
--------------------------------------------------------------------------------
|  ACB   |  1832  |   2019-04-22  |   9.1 $   |   8.68 $  | -769.44 $ |-4.62 % |
|  AMD   |  597   |   2019-04-22  | 27.9316 $ |   27.5 $  | -257.67 $ |-1.55 % |
|  MBRX  | 11261  |   2019-04-22  |   1.48 $  |   1.16 $  | -3603.52 $|-21.62 %|
|  KEYW  |  1487  |   2019-04-22  |  11.21 $  |  11.22 $  |  14.87 $  | 0.09 % |
|  RAD   |  1718  |   2019-04-22  |  9.7006 $ |   9.13 $  | -980.29 $ |-5.88 % |
|  STLD  |  500   |   2019-04-22  |  33.335 $ |  30.02 $  | -1657.5 $ |-9.94 % |
| Total  |   NA   |   2019-04-22  | 100015.0 $| 92761.5 $ | -7253.5 $ |-7.25 % |
--------------------------------------------------------------------------------
```

Whenever you measure returns, the output is saved as a report into the database,
you can access it with `report`:
```shell
(beta): report
----------------------------------------------------------------------
| Pos |    Id    |           Date          |           Name          |
----------------------------------------------------------------------
|  1  |    1     |        2019-04-26       |       6 Big Stuffs      |
|  2  |    2     |        2019-04-27       |       6 Big Stuffs      |
|  3  |    3     |        2019-04-27       |           Test          |
|  4  |    4     |        2019-04-27       |       6 Big Stuffs      |
|  5  |    5     |        2019-04-28       |         One One         |
|  6  |    6     |        2019-05-18       |   Glorious Investment   |
|  7  |    7     |        2019-05-19       |       6 Big Stuffs      |
----------------------------------------------------------------------
--> Report ID ? (Id): 1
```
