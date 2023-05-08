from TradingBot.Exchanges.Kraken import Kraken
from TradingBot.Exchanges.Kucoin import Kucoin
from TradingBot.Exchanges.Gate import Gate
from TradingBot.Exchanges.Binance import Binance
from TradingBot.Exchanges.BinanceUS import BinanceUS
from TradingBot.Exchanges.Bittrex import Bittrex
from TradingBot.Exchanges.CoinbasePro import CoinbasePro
from TradingBot.Exchanges.Gemini import Gemini

# Type Hinting
from typing import Dict, List, Union, Optional, Any


def execute(exchange: str, api_keys: dict, orderid: str, symbol: str) -> Union[Dict, List]:
    
    if exchange.lower() == "binance":
        api = Binance(api_keys['api_key'], api_keys['api_secret'])
        url_path = "/api/v3/order"
        method = "DELETE"
        payload = {
            "symbol": symbol,
            "orderId": orderid,
        }
        r = api.send_signed_request(http_method = method, url_path = url_path, payload = payload)
        print("Order Cancelled: ", r)
        return r
    
    elif exchange.lower() == "kraken":
        
        # initialize the trading bot
        api = Kraken(api_keys['api_key'], api_keys['api_secret'])
        
        # prepare the parameters
        url_method = 'CancelOrder'
        p = {
            'txid': orderid
        }
        # execute the order
        r = api.send_signed_request(url_method, p)
        print("Order Cancelled: ", r)
        return r
        
    
    elif exchange.lower() == "kucoin":
        
        api = Kucoin(api_keys['api_key'], api_keys['api_secret'], api_keys['passphrase'])
        url = f'/api/v1/orders/{orderid}'
        params = {
            'orderId': orderid
        }
        method = 'DELETE'
        r = api.send_signed_request(uri_path=url, params = params, method = method)
        print("Order Cancelled: ", r)
        return r
        
    
    elif exchange.lower() == "gate":
        
        api = Gate(api_keys['api_key'], api_keys['api_secret'])
        url = f'/spot/price_orders/{orderid}'
        query_param = {}
        body = {}
        
        method = 'DELETE'
        r = api.send_signed_request(url = url, query_param = query_param, body = body, method = method)
        print("Order Cancelled: ", r)
        return r

    elif exchange.lower() == "binanceus":
        api = BinanceUS(api_keys['api_key'], api_keys['api_secret'])
        url_path = "/api/v3/order"
        method = "DELETE"
        payload = {
            "symbol": symbol,
            "orderId": orderid,
        }
        r = api.send_signed_request(http_method = method, url_path = url_path, payload = payload)
        print("Order Cancelled: ", r)
        return r

    elif exchange.lower() == "coinbasepro":
        # initialize the trading bot
        api = CoinbasePro(api_keys['api_key'], api_keys['api_secret'], api_keys['passphrase'],base_url='https://api.coinbase.com/api/v3/brokerage/')
        url_path = 'orders/batch_cancel/'
        method = 'POST'
        data = {
            "order_ids": orderid
        }
        params = {}
        r = api.send_signed_request(method = method, endpoint = url_path, params = params, data = data)
        return r

    elif exchange.lower() == "bittrex":

        # initialize the trading bot
        api = Bittrex(api_keys['api_key'], api_keys['api_secret'])
        url_path = f'/orders/{orderid}'
        payload = {
            "orderId": orderid
        }
        method = 'DELETE'
        r = api.send_signed_request(method = method, path=url_path, params=payload)
        return r

    elif exchange.lower() == "gemini":
            
        # initialize the trading bot
        api = Gemini(api_keys['api_key'], api_keys['api_secret'])
        url_path = '/v1/order/new'
        payload = params
        method = 'POST'
        
        r = api.send_signed_request(method = method, url_path=url_path, param=payload)
        return r
        
        
        


