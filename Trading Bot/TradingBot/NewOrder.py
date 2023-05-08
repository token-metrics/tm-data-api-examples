from TradingBot.Exchanges.Kraken import Kraken
from TradingBot.Exchanges.Kucoin import Kucoin
from TradingBot.Exchanges.Gate import Gate
from TradingBot.Exchanges.Binance import Binance
from TradingBot.Exchanges.BinanceUS import BinanceUS
from TradingBot.Exchanges.Bittrex import Bittrex
from TradingBot.Exchanges.CoinbasePro import CoinbasePro
from TradingBot.Exchanges.Gemini import Gemini

from typing import Dict, List, Union, Optional, Any


## other essential packages
# kucoin
from uuid import uuid1

def execute(exchange: str, api_keys: Dict[str, str], params: Dict[str, str]) -> Any:
    """A function to execute a new order on the exchange.

    Args:
        exchange (str): The exchange name.
        api_keys (Dict[str, str]): API keys for the exchange.
        params (Dict[str, str]): A dictionary of parameters for the order.

    Returns:
        Any: The response from the exchange.
    """
    
    if exchange.lower() == "binance":
        
        # initialize the trading bot
        api = Binance(api_keys['api_key'], api_keys['api_secret'])
        url_path = '/api/v3/order'
        method = 'POST'
        payload = params
        r = api.send_signed_request(http_method = method, url_path = url_path, payload = payload)
        return r
    
    elif exchange.lower() == "kraken":
        
        # initialize the trading bot
        api = Kraken(api_keys['api_key'], api_keys['api_secret'])
        
        # prepare the parameters
        url_method = 'AddOrder'
        
        # execute the order
        response = api.send_signed_request(url_method, params)
        
        return response
    
    elif exchange.lower() == "kucoin":
        
        # initialize the trading bot, inputs are api_keys and passphrase
        api = Kucoin(api_keys['api_key'], api_keys['api_secret'], api_keys['passphrase'])
        
        # parse the parameters
        url_path = '/api/v1/orders'
        method = 'POST'
        
        # give the clientOid
        clientOid = ''.join([each for each in str(uuid1()).split('-')])
        params['clientOid'] = clientOid
        
        # execute the order
        response = api.send_signed_request(uri_path = url_path, params = params, method = method)
        return response
    
    elif exchange.lower() == "gate":
        
        # initialize the trading bot
        api = Gate(api_keys['api_key'], api_keys['api_secret'])
        
        # send signed request
        url = '/spot/orders'
        query_param = ''
        body = params
        method = 'POST'
        r = api.send_signed_request(url = url, query_param = query_param, body = body, method = method)
        
        return r
        
    elif exchange.lower() == "binanceus":
           
        # initialize the trading bot
        api = BinanceUS(api_keys['api_key'], api_keys['api_secret'])
        url_path = '/api/v3/order'
        method = 'POST'
        payload = params
        r = api.send_signed_request(http_method = method, url_path = url_path, payload = payload)
        return r

    elif exchange.lower() == "coinbasepro":
           
        # initialize the trading bot
        api = CoinbasePro(api_keys['api_key'], api_keys['api_secret'], api_keys['passphrase'],base_url='https://api.coinbase.com/api/v3/brokerage/')
        url_path = 'orders'
        method = 'POST'
        data = params
        params = {}
        r = api.send_signed_request(method = method, endpoint = url_path, params = params, data = data)
        return r

    elif exchange.lower() == "bittrex":

        # initialize the trading bot
        api = Bittrex(api_keys['api_key'], api_keys['api_secret'])

        url_path = '/orders'
        payload = params
        method = 'POST'

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
        


