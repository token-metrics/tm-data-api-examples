import hmac
import time
import hashlib
import requests
from urllib.parse import urlencode
import typing


class BinanceUS():
    def __init__(self, api_key: str = None, api_secret: str = None, BASE_URL :str = 'https://api.binance.us'):
        self.BASE_URL = BASE_URL
        self.KEY = api_key
        self.SECRET = api_secret
        

    ''' ======  begin of functions, you don't need to touch ====== '''
    def hashing(self,query_string):
        return hmac.new(self.SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    def get_timestamp(self):
        return int(time.time() * 1000)


    def dispatch_request(self,http_method):
        session = requests.Session()
        session.headers.update({
            'Content-Type': 'application/json;charset=utf-8',
            'X-MBX-APIKEY': self.KEY
        })
        return {
            'GET': session.get,
            'DELETE': session.delete,
            'PUT': session.put,
            'POST': session.post,
        }.get(http_method, 'GET')

    # used for sending request requires the signature
    def send_signed_request(self, http_method, url_path, payload={}):
        query_string = urlencode(payload, True)
        
        if query_string:
            query_string = "{}&timestamp={}".format(query_string, self.get_timestamp())
        else:
            query_string = 'timestamp={}'.format(self.get_timestamp())

        url = self.BASE_URL + url_path + '?' + query_string + '&signature=' + self.hashing(query_string)
        # print("{} {}".format(http_method, url))
        params = {'url': url, 'params': {}}
        response = self.dispatch_request(http_method)(**params)
        return response.json()

    # used for sending public data request
    def send_public_request(self, url_path, payload={}):
        query_string = urlencode(payload, True)
        url = self.BASE_URL + url_path
        if query_string:
            url = url + '?' + query_string
        # print("{}".format(url))
        # response = dispatch_request('GET')(url=url)
        response = requests.get(url)
        return response.json()

    ''' ======  end of functions ====== '''
    
if __name__ == '__main__':
    
    pass
