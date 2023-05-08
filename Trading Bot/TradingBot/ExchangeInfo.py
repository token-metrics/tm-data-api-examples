import requests
from pandas import json_normalize


def execute(exchange: str):
    
    if exchange.lower() == "binance":

        r = requests.get('https://api.binance.com/api/v3/exchangeInfo')
        try:
            return json_normalize(r.json()['symbols'])
        except:
            return r.json()
        
    elif exchange.lower() == "kraken":
        r = requests.get('https://api.kraken.com/0/public/AssetPairs')
        return json_normalize(r.json()['result'].values())
    
    elif exchange.lower() == "kucoin":
        r = requests.get('https://api.kucoin.com/api/v1/symbols')
        return json_normalize(r.json()['data'])
    
    elif exchange.lower() == "gate":
        r = requests.get("https://api.gateio.ws/api/v4/spot/currency_pairs")
        return json_normalize(r.json())

    elif exchange.lower() == "binanceus":
        r = requests.get('https://api.binance.us/api/v3/exchangeInfo')
        return json_normalize(r.json()['symbols'])

    elif exchange.lower() == "gemini":
        base_url = "https://api.gemini.com/v1"
        response = requests.get(base_url + "/symbols")
        symbols = response.json()
        exchange_info = []

        for smb in symbols:
            base_url = "https://api.gemini.com/v1"
            response = requests.get(base_url + f"/symbols/details/{smb}")
            symbols = response.json()
            exchange_info.append(symbols)

        return json_normalize(exchange_info)

    elif exchange.lower() == "coinbasepro":
        r = requests.get('https://api.exchange.coinbase.com/products')
        return json_normalize(r.json())

    elif exchange.lower() == "bittrex":
        r = requests.get("https://api.bittrex.com/v3/markets")
        return json_normalize(r.json())
        
        
        


