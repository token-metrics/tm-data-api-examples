import TradingBot as tb
from API_keys import api_keys
    
# #* create an order
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


# #* get the exchange info - finished
# bot = tb.Bot(exchange='Binance')
# print(bot.get_ExchangeInfo())

# bot = tb.Bot(exchange='BinanceUS')
# print(bot.get_ExchangeInfo())

# bot = tb.Bot(exchange='Kraken')
# print(bot.get_ExchangeInfo())

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


# #* get account info - finished
# exchange = 'Kucoin'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

# exchange = 'BinanceUS'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

# exchange = 'Binance'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

# exchange = 'Kraken'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_AccountInfo())

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


# #* get ticker info - finished
# bot = tb.Bot(exchange='Binance')
# symbol = 'BTCUSDT' # for Binance
# print(bot.get_TickerInfo(symbol))

# bot = tb.Bot(exchange='BinanceUS')
# symbol = 'BTCUSDT' # for BinanceUS
# print(bot.get_TickerInfo(symbol))

# bot = tb.Bot(exchange='Gate')
# symbol = 'BTC_USDT' # for Gate
# print(bot.get_TickerInfo(symbol))

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


# #* get open orders info
# exchange = 'Kucoin'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

# exchange = 'Gate'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

# exchange = 'Kraken'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# print(bot.get_OpenOrderInfo())

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


# #* cancel an order
# exchange = 'Gate'
# bot = tb.Bot(exchange=exchange, api_keys=api_keys[exchange])
# orderid = '12345123'
# print(bot.make_CancelOrder(orderid))

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





