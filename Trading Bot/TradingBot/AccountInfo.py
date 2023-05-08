from TradingBot.Exchanges.Kraken import Kraken
from TradingBot.Exchanges.Kucoin import Kucoin
from TradingBot.Exchanges.Gate import Gate
from TradingBot.Exchanges.Binance import Binance
from TradingBot.Exchanges.BinanceUS import BinanceUS
from TradingBot.Exchanges.Bittrex import Bittrex
from TradingBot.Exchanges.CoinbasePro import CoinbasePro
from TradingBot.Exchanges.Gemini import Gemini
from pandas import json_normalize


def execute(exchange: str, api_keys: dict):
    
    if exchange.lower() == "binance":
        
        api = Binance(api_keys['api_key'], api_keys['api_secret'],BASE_URL = 'https://api.binance.com')
        url_path = '/api/v3/account'
        payload = {
        }
        method = 'GET'
        r = api.send_signed_request(http_method = method, url_path = url_path, payload = payload)

        return r
    
    elif exchange.lower() == "kraken":
        
        # initialize the trading bot
        api = Kraken(api_keys['api_key'], api_keys['api_secret'])
        
        # prepare the parameters
        url_method = 'Balance'
        params = {}
        # execute the order
        r = api.send_signed_request(url_method, params)
        
        return r
        # r = json_normalize(r['result']).T.rename(columns={0: 'Balance'}).astype(float).round(4).sort_values(by='Balance', ascending=False)
        # return r[r.Balance != 0]
    
    elif exchange.lower() == "kucoin":
        
        api = Kucoin(api_keys['api_key'], api_keys['api_secret'], api_keys['passphrase'])
        url = '/api/v1/accounts'
        params = {}
        method = 'GET'
        
        r = api.send_signed_request(uri_path=url, params = params, method = method)
        return r
        # return r[r.balance != 0]
        
    
    elif exchange.lower() == "gate":
        
        api = Gate(api_keys['api_key'], api_keys['api_secret'])
        url = '/spot/accounts'
        query_param = {}
        body = {}
        method = 'GET'
        r = api.send_signed_request(url = url, query_param = query_param, body = body, method = method)
        return r
        # return json_normalize(r[0]['available'])
        
    elif exchange.lower() == "binanceus":
            
        api = BinanceUS(api_keys['api_key'], api_keys['api_secret'],BASE_URL = 'https://api.binance.us')
        url_path = '/api/v3/account'
        payload = {}
        method = 'GET'
        r = api.send_signed_request(http_method = method, url_path = url_path, payload = payload)
        return r

    elif exchange.lower() == "bittrex":
        api = Bittrex(api_keys['api_key'], api_keys['api_secret'])
        url_path = '/balances'
        payload = {
        }
        method = 'GET'
        r = api.send_signed_request(method, url_path, payload)
        return r

    elif exchange.lower() == "coinbasepro":
        api = CoinbasePro(api_keys['api_key'], api_keys['api_secret'], api_keys['passphrase'])
        path = 'accounts'
        payload = {}
        r = api.send_signed_request('GET', path, payload)
        return r

    elif exchange.lower() == "gemini":
        api = Gemini(api_keys['api_key'], api_keys['api_secret'])
        url_path = '/v1/balances'
        param = {
            'account': 'primary'
                }
        r = api.send_signed_request(url_path = url_path, param = param)
        return r
        


