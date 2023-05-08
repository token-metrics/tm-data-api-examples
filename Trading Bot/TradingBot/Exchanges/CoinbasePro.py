# Reference: https://github.com/danpaquin/coinbasepro-python/tree/master/cbpro

import time
import urllib.parse
from typing import Optional, Dict, Any, List
import hmac
import requests
from urllib.parse import urlencode
import hashlib
import base64

import json

class CoinbasePro:

    def __init__(self, api_key=None, api_secret=None, passphrase=None, base_url = 'https://api.exchange.coinbase.com/') -> None:
        
        self._api_key = api_key
        self._api_secret = api_secret
        self._passphrase = passphrase
        self._BASE_URL = base_url

    def _sign_request(self, timestamp, request):
        message = timestamp + request.method + request.path_url +  (request.body or '')
        message = message.encode('ascii')
        hmac_key = base64.b64decode(self._api_secret)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
        
        return signature_b64


    def send_signed_request(self, method, endpoint, params, data = ''):
        timestamp = str(time.time())
        endpoint = endpoint  if endpoint.endswith('/') else endpoint + '/'
        url = self._BASE_URL + endpoint
        print(url)
        if data:
            data = json.dumps(data)
        req = requests.Request(method = method, url = url, params=params, data=data)
        request = req.prepare()
        signature_b64 = self._sign_request(timestamp, request)

        request.headers.update({
        # 'User-Agent': 'python-requests/2.27.1', 
        # 'Accept-Encoding': 'gzip, deflate, br', 
        'accept': 'application/json',
        # 'Connection': 'keep-alive',
        'Content-Type': 'Application/JSON',
        'CB-ACCESS-SIGN': signature_b64,
        'CB-ACCESS-TIMESTAMP': timestamp,
        'CB-ACCESS-KEY': self._api_key,
        'CB-ACCESS-PASSPHRASE': self._passphrase
    })
        s = requests.Session()
        r = s.send(request)

        return r.text

    def send_public_request(self, url_path, payload={}):
        query_string = urlencode(payload, True)
        url = self._BASE_URL + url_path
        if query_string:
            url = url + '?' + query_string
        # print("{}".format(url))
        # response = dispatch_request('GET')(url=url)
        response = requests.get(url)
        return response.json()

if __name__ == '__main__':
    pass






