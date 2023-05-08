# Step4 Trading Bot in real account

## Table of Content

* [Description](#description)
* [Installation](#installation)
* [Folder Structure](#folder-structure)
* [Set your API key](#set-your-api-key)
* [Practice: Get the exchange information](#practice--get-the-exchange-information)
* [Practice: Get ticker info](#practice--get-ticker-info)
* [Practice: Get account info](#practice--get-account-info)
* [Practice: Create an order](#practice--create-an-order)
* [Practice: Get open orders info](#practice--get-open-orders-info)
* [Practice: Cancel an order](#practice--cancel-an-order)
* [Put them together and implement them!](#put-them-together-and-implement-them-)


## Description

This API module is designed to help trading automation over different exchanges, especially in cryptocurrency exchanges, where this frame could be expanded to most of the mainstream exchanges.

Currently, we have supported the following exchanges:

- Binance
- Coinbase Pro
- Binance US
- Okx
- Kraken
- Kucoin
- Gate
- Bittrex
- Gemini

## Installation

```bash
git clone https://github.com/token-metrics/tm-data-api-examples.git

cd tm-data-api-examples/Trading\ Bot
```

## Folder Structure

```bash
.
├── API_keys.py      # Input your API key
├── TradingBot     	 # TradingBot Module
└── example.py     	 # Code Example
```

## Set your API key

`API_keys.py`

```python
api_keys = {
    "Binance": {
        "api_key": "<your api key>",
        "api_secret": "<your api key>"
    },
    "Kraken": {
        "api_key": "<your api key>",
        "api_secret": "<your api key>"
    },
    "Kucoin": {
        "api_key": "<your api key>",
        "api_secret": "<your api key>",
        "passphrase": "<your api key>"
    },
    "Gate": {
        "api_key": "<your api key>",
        "api_secret": "<your api key>",
    },
    "BinanceUS": {
        "api_key": "<your api key>",
        "api_secret": "<your api key>",
    },
    "Gemini": {
        "api_key": "<your api key>",
        "api_secret": "<your api key>",
    },
    "CoinbasePro": {
        "api_key": "<your api key>",
        "api_secret": "<your api key>",
        "passphrase": "<your api key>"
    },
    'Bittrex': {
        'api_key': '<your api key>',
        'api_secret': '<your api key>'
    },

}
```

## Practice: Get the exchange information

`example.py`


```python
import TradingBot as tb

# bot = tb.Bot(exchange='Binance')
# print(bot.get_ExchangeInfo())

# bot = tb.Bot(exchange='BinanceUS')
# print(bot.get_ExchangeInfo())

bot = tb.Bot(exchange='Kraken')
print(bot.get_ExchangeInfo())

# bot = tb.Bot(exchange='Kucoin')
# print(bot.get_ExchangeInfo())

# bot = tb.Bot(exchange='Gate')
# print(bot.get_ExchangeInfo())

# bot = tb.Bot(exchange='Gemini')
# print(bot.get_ExchangeInfo())

# bot = tb.Bot(exchange='CoinbasePro')
# print(bot.get_ExchangeInfo())

# bot = tb.Bot(exchange='Bittrex')
# print(bot.get_ExchangeInfo())
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>altname</th>
      <th>wsname</th>
      <th>aclass_base</th>
      <th>base</th>
      <th>aclass_quote</th>
      <th>quote</th>
      <th>lot</th>
      <th>pair_decimals</th>
      <th>lot_decimals</th>
      <th>lot_multiplier</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1INCHEUR</td>
      <td>1INCH/EUR</td>
      <td>currency</td>
      <td>1INCH</td>
      <td>currency</td>
      <td>ZEUR</td>
      <td>unit</td>
      <td>3</td>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1INCHUSD</td>
      <td>1INCH/USD</td>
      <td>currency</td>
      <td>1INCH</td>
      <td>currency</td>
      <td>ZUSD</td>
      <td>unit</td>
      <td>3</td>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AAVEAUD</td>
      <td>AAVE/AUD</td>
      <td>currency</td>
      <td>AAVE</td>
      <td>currency</td>
      <td>ZAUD</td>
      <td>unit</td>
      <td>2</td>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AAVEETH</td>
      <td>AAVE/ETH</td>
      <td>currency</td>
      <td>AAVE</td>
      <td>currency</td>
      <td>XETH</td>
      <td>unit</td>
      <td>4</td>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AAVEEUR</td>
      <td>AAVE/EUR</td>
      <td>currency</td>
      <td>AAVE</td>
      <td>currency</td>
      <td>ZEUR</td>
      <td>unit</td>
      <td>2</td>
      <td>8</td>
      <td>1</td>
    </tr>
  </tbody>
</table>



## Practice: Get ticker info


```python
# bot = tb.Bot(exchange='Binance')
# symbol = 'BTCUSDT' # for Binance
# print(bot.get_TickerInfo(symbol))

# bot = tb.Bot(exchange='BinanceUS')
# symbol = 'BTCUSDT' # for BinanceUS
# print(bot.get_TickerInfo(symbol))

bot = tb.Bot(exchange='Gate')
symbol = 'BTC_USDT' # for Gate
print(bot.get_TickerInfo(symbol))

# bot = tb.Bot(exchange='Kraken')
# symbol = 'XBTUSD' # for Kraken
# print(bot.get_TickerInfo(symbol))

# bot = tb.Bot(exchange='Kucoin')
# symbol = 'BTC-USDT' # for Kucoin
# print(bot.get_TickerInfo(symbol))

# bot = tb.Bot(exchange='Gemini')
# symbol = 'btcusd' # for Gemini
# print(bot.get_TickerInfo(symbol))

# bot = tb.Bot(exchange='CoinbasePro')
# symbol = 'BTC-USD' # for CoinbasePro
# print(bot.get_TickerInfo(symbol))

# bot = tb.Bot(exchange='Bittrex')
# symbol = 'BTC-USD' # for Bittrex
# print(bot.get_TickerInfo(symbol))
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>currency_pair</th>
      <th>last</th>
      <th>lowest_ask</th>
      <th>highest_bid</th>
      <th>change_percentage</th>
      <th>base_volume</th>
      <th>quote_volume</th>
      <th>high_24h</th>
      <th>low_24h</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BTC_USDT</td>
      <td>23559.03</td>
      <td>23559.03</td>
      <td>23559.02</td>
      <td>2.25</td>
      <td>6148.612962762</td>
      <td>144155966.35896</td>
      <td>24173.5</td>
      <td>22666</td>
    </tr>
  </tbody>
</table>

## Practice: Get account info


```python
# exchange = 'Kucoin'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

# exchange = 'BinanceUS'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

# exchange = 'Binance'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

exchange = 'Kraken'
bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
print(bot.get_AccountInfo())

# exchange = 'Gate'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

# exchange = 'Bittrex'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

# exchange = 'CoinbasePro'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

# exchange = 'Gemini'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Balance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>USDC</th>
      <td>800100.0000</td>
    </tr>
    <tr>
      <th>ZUSD</th>
      <td>774984.4626</td>
    </tr>
    <tr>
      <th>MATIC</th>
      <td>42112.0000</td>
    </tr>
    <tr>
      <th>DOT</th>
      <td>5936.0000</td>
    </tr>
    <tr>
      <th>UNI</th>
      <td>5509.1800</td>
    </tr>
  </tbody>
</table>

## Practice: Create an order


```python
# #! Kraken
# bot = tb.Bot(api_keys = api_keys['Kraken'])
# commands = {
#     "public_params":{
#         "symbol": "BCHUSD",
#         "side":"buy",
#         "type":"limit",
#         "quantity": "1",
#         "price":"50",
#         "stopPrice":"",
#     },
#     "private_params":{
#     }
# }

# print(bot.bot_status())
# print(bot.switch_exchange('Kraken'))
# print(bot.bot_status())
# bot.new_Order(commands)

    
# #! Kucoin
# bot = tb.Bot('Kucoin', api_keys['Kucoin'])
# commands = {
#     "public_params":{
#         "symbol": "BTC-USDT",
#         "side":"buy",
#         "type":"limit",
#         "quantity": "0.001",
#         "price":"12000",
#         "stopPrice":"", 
#     },
#     "private_params":{
#         "cancelAfter":"",
#     }
# }
# print(bot.bot_status())
# bot.new_Order(commands)

# # ! Gate
# bot = tb.Bot('Gate', api_keys['Gate'])
# commands = {
#     "public_params":{
#         "symbol": "BTC_USDT",
#         "side":"buy",
#         "type":"limit",
#         "quantity": "0.001",
#         "price":"12000",
#         "stopPrice":"", # The Gate does not support stopPrice
#     },
#     "private_params":{
#     }
# }
# print(bot.bot_status())
# bot.new_Order(commands)


# #! Binance
# bot = tb.Bot('Binance', api_keys['Binance'])
# commands = {
#     "public_params":{
#         "symbol": "DOGEUSDT",
#         "side":"sell",
#         "type":"limit",
#         "quantity": "100",
#         "price":"0.1",
#         "stopPrice":"", 
#     },
#     "private_params":{
#         "timeInForce": "GTC",
#     }
# }
# bot.new_Order(commands)

# #! BinanceUS
# bot = tb.Bot('BinanceUS', api_keys['BinanceUS'])
# commands = {
#     "public_params":{
#         "symbol": "DOGEUSDT",
#         "side":"sell",
#         "type":"limit",
#         "quantity": "100",
#         "price":"0.1",
#         "stopPrice":"", 
#     },
#     "private_params":{
#         "timeInForce": "GTC",
#     }
# }
# bot.new_Order(commands)

# #!Bittrex

# bot = tb.Bot('Bittrex', api_keys['Bittrex'])
# commands = {
#     "public_params":{
#         "symbol": "1INCH-USDT",
#         "side":"BUY",
#         "type":"LIMIT",
#         "quantity": 10,
#         "price":1,
#         "stopPrice":"", 
#     },
#     "private_params":{
#         "timeInForce": "GOOD_TIL_CANCELLED",
#     }
# }
# bot.new_Order(commands)

# #! CoinbasePro
# bot = tb.Bot('CoinbasePro', api_keys['CoinbasePro'])

# commands = {
#     "public_params":{
#         "symbol": "ETH-USDT",
#         "side":"BUY",
#         "type":"LIMIT",
#         "quantity": 1200,
#         "price":1,
#         "stopPrice":"", 
#     },
#     "private_params":{
#         "timeInForce": "GTC",
#     }
# }
# bot.new_Order(commands)

# # ! Gemini
# bot = tb.Bot('Gemini', api_keys['Gemini'])
# commands = {
#     "public_params":{
#         "symbol": "btcusd",
#         "side":"buy",
#         "type":"exchange limit",
#         "quantity": '0.01',
#         "price":'20000',
#         "stopPrice":"", 
#     },
#     "private_params":{    
#     }
# }
# bot.new_Order(commands)
```

## Practice: Get open orders info


```python
# exchange = 'Kucoin'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

# exchange = 'Gate'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

exchange = 'Kraken'
bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
print(bot.get_OpenOrderInfo())

# exchange = 'Binance'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

# exchange = 'BinanceUS'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

# exchange = 'Bittrex'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

# exchange = 'CoinbasePro'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

# exchange = 'Gemini'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>OrderID</th>
      <th>stopprice</th>
      <th>limitprice</th>
      <th>misc</th>
      <th>oflags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ON6CLT-GDZYI-W7YOVV</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td></td>
      <td>fciq</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OFLB7Q-YFAUF-U735F2</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td></td>
      <td>fciq</td>
    </tr>
    <tr>
      <th>2</th>
      <td>OMP2G7-FFWZO-GBJ4ZH</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td></td>
      <td>fciq</td>
    </tr>
    <tr>
      <th>3</th>
      <td>O5WQIS-2MQY7-ONDU4B</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td></td>
      <td>fciq</td>
    </tr>
    <tr>
      <th>4</th>
      <td>OFYZZ7-J3I42-KJJF2X</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td></td>
      <td>fciq</td>
    </tr>
  </tbody>
</table>

## Practice: Cancel an order


```python
exchange = 'Gate'
bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
orderid = '12345123'
print(bot.make_CancelOrder(orderid))

# exchange = 'Binance'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# orderid = '12345123'
# symbol = 'BTCUSDT'
# print(bot.make_CancelOrder(orderid,symbol))

# exchange = 'BinanceUS'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# orderid = '12345123'
# symbol = 'BTCUSDT'
# print(bot.make_CancelOrder(orderid,symbol))

# exchange = 'Kraken'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# orderid = '12345123'
# print(bot.make_CancelOrder(orderid))

# exchange = 'Kucoin'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# orderid = '12345123'
# print(bot.make_CancelOrder(orderid))

# exchange = 'CoinbasePro'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# orderid = '12345123'
# print(bot.make_CancelOrder(orderid))

# exchange = 'Bittrex'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# orderid = '12345123'
# print(bot.make_CancelOrder(orderid))

# exchange = 'Gemini'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# orderid = '12345123'
# print(bot.make_CancelOrder(orderid))
```

    Order Cancelled:  {'label': 'ORDER_NOT_FOUND', 'message': 'not found order info id:12345123 count:0'}
    True

# Put them together and implement them!

Now, with the Trading Bot, we have the capabilities to do the followings:

1. Obtain the price of the `BTC`
2. Monitor our account balance
3. Create and cancel the order

Amazing, the remaining thing is simple, just code your trading logic as we do during the backtesting process:

```python
  if we do not hold position: 
      if it is a buy signal: 
          we buy!!! --> Long position

      else it is a sell signal:
          we sell!!! --> Short position

  else if we hold the short position:

      we closed our short position

  else if we hold the long position:

      we closed our long position
```

Beyond the Moon!



