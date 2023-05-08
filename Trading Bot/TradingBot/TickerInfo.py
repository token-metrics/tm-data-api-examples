import requests
from pandas import json_normalize
import typing


def execute(exchange: str, symbol: str):

    
    if exchange.lower() == "binance":
        
        params = {'symbol':symbol} 
        priceTicker = requests.get('https://api.binance.com/api/v3/ticker/price', params=params).json()
        orderTicker = requests.get('https://api.binance.com/api/v3/ticker/bookTicker', params=params).json()
        priceTicker.update(orderTicker)

        return priceTicker
    
    elif exchange.lower() == "kraken":
        # reference: https://support.kraken.com/hc/en-us/articles/360000920306-API-symbols-and-tickers
        # https://algotrading101.com/learn/kraken-api-guide/

        '''
        index =  pair name

        a = ask array(<price>, <whole lot volume>, <lot volume>)

        b = bid array(<price>, <whole lot volume>, <lot volume>)

        c = last trade closed array(<price>, <lot volume>)

        v = volume array(<today>, <last 24 hours>)

        p = volume weighted average price array(<today>, <last 24 hours>)

        t = number of trades array(<today>, <last 24 hours>)

        l = low array(<today>, <last 24 hours>)

        h = high array(<today>, <last 24 hours>)

        o = today’s opening price

        '''

        r = requests.get(f'https://api.kraken.com/0/public/Ticker?pair={symbol}').json()

        if not r['error']:
            r = r['result']
            r = r[list(r.keys())[0]]
            r = {k:float(v[0]) if isinstance(v, list) else float(v) for k,v in r.items()}

            r['ask'] = r.pop('a')
            r['bid'] = r.pop('b')
            r['last price'] = r.pop('c')
            r['volume'] = r.pop('v')
            r['volume weighted average price'] = r.pop('p')
            r['number of trades'] = r.pop('t')
            r['lowest price'] = r.pop('l')
            r['highest price'] = r.pop('h')
            r['opening price'] = r.pop('o')
            
            return r
        else:
            return r
    
    elif exchange.lower() == "kucoin":

        r = requests.get(f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}").json()
        return r['data'] if r['data'] else r

    
    elif exchange.lower() == "gate":

        params = {'currency_pair': symbol,}
        r = requests.get("https://api.gateio.ws/api/v4/spot/tickers", params=params)
        return r.json()

    elif exchange.lower() == "binanceus":

        params = {'symbol':symbol} 
        priceTicker = requests.get('https://api.binance.us/api/v3/ticker/price', params=params).json()
        orderTicker = requests.get('https://api.binance.us/api/v3/ticker/bookTicker', params=params).json()
        priceTicker.update(orderTicker)

        return priceTicker

    elif exchange.lower() == "gemini":

        base_url = f"https://api.gemini.com/v1/pubticker/{symbol}"
        r = requests.get(base_url).json()
        r['lastprice'] = r.pop('last')
        return r


    elif exchange.lower() == "coinbasepro":
        r = requests.get(f'https://api.exchange.coinbase.com/products/{symbol}/ticker')
        return r.json()

    elif exchange.lower() == "bittrex":
        r = requests.get(f"https://api.bittrex.com/v3/markets/{symbol}/ticker").json()
        r['lastprice'] = r.pop('lastTradeRate')
        return r




