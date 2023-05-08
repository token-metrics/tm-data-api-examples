# author: Cholian Li
# Date: 20220713
# Email: cholianli970518@gmail.com

from urllib.parse import urlencode
import requests
import time
import urllib.parse
import hmac
import hashlib
import json



class Bitmex():
    def __init__(self, api_key = None, api_secret = None, BASE_URL = None, headers = None):
        self.BASE_URL = BASE_URL or 'https://www.bitmex.com/api/v1'
        self.KEY = api_key
        self.SECRET = api_secret
        self.headers = headers or {'content-type': 'application/json'}
        
        
    def generate_signature(self, secret, verb, url, expires, data):
        """Generate a request signature compatible with BitMEX."""
        # Parse the url so we can remove the base and extract just the path.
        parsedURL = urllib.parse.urlparse(url)
        path = parsedURL.path
        if parsedURL.query:
            path = path + '?' + parsedURL.query

        if isinstance(data, (bytes, bytearray)):
            data = data.decode('utf8')

        message = bytes(verb + path + str(expires) + data, 'utf-8')
        print("Computing HMAC: %s" % message)

        signature = hmac.new(bytes(secret, 'utf-8'), message, digestmod=hashlib.sha256).hexdigest()
        return signature
        
    # used for sending public data request
    def send_public_request(self, url_path, param=''):
        query_string = urlencode(param, True)
        url = self.BASE_URL + url_path
        if query_string:
            url = url + '?' + query_string
            
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    # send private data request
    def send_signed_request(self, end_point, param = '', method = 'GET'):

        verb = method
        path = '/api/v1' + end_point
        expires = int(round(time.time()) + 5)
        # expires = 1518064238 # 2018-02-08T04:30:38Z 
        
        if param:
            data = json.dumps(param).replace(" ", "")
        else: 
            data = ''
        print(self.SECRET, verb, path, expires, data)
        gen_sign = self.generate_signature(self.SECRET, verb, path, expires, data)
        
        
        url = self.BASE_URL + end_point
        self.headers.update({
            'api-expires': str(expires),
            'api-key': self.KEY,
            'api-signature': str(gen_sign),
            })
        print(self.headers)
        r = requests.request(method, url, headers=self.headers, data=param)
        return r.json()



if __name__ == '__main__':
    
    pass