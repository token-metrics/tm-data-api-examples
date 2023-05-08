import time
import hashlib
import hmac
import requests
import json
from urllib.parse import urlencode

class Gate(object):
    def __init__(self, key = '', secret='', host = '', prefix = ''):
        self.key = key
        self.secret = secret
        self.host = host or "https://api.gateio.ws"
        self.prefix = prefix or "/api/v4"
        
    def gen_sign(self, method, url, query_string=None, payload_string=None):
        
        t = time.time()
        # t = '1656298733.328256'
        m = hashlib.sha512()
        m.update((payload_string or "").encode('utf-8'))
        hashed_payload = m.hexdigest()
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
        sign = hmac.new(self.secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'KEY': self.key, 'Timestamp': str(t), 'SIGN': sign}    
    
    def send_signed_request(self, url, query_param = {}, body = {}, method = 'GET', headers = None):
        headers = headers or {'Accept': 'application/json', 'Content-Type': 'application/json'}
        
        if query_param:
            query_param = urlencode(query_param, True)
        else: 
            query_param = ''
        
        if body:
            body = json.dumps(body)
            
        else:
            body = ''
        
        # print(method, self.prefix + url, query_param, body)
        sign_headers = self.gen_sign(method, self.prefix + url, query_param, body) 
        headers.update(sign_headers)
        # print(sign_headers)
        
        if query_param:
            request_url = self.host + self.prefix + url + "?" + query_param
        else:
            request_url = self.host + self.prefix + url
        
        r = requests.request(method, request_url, headers=headers, data=body)
        return r.json()
    
    def send_public_request(self, url, query_param = '',headers = None):
        headers = headers or {'Accept': 'application/json', 'Content-Type': 'application/json'}
        
        if query_param:
            query_param = urlencode(query_param, True)
            request_url = self.host + self.prefix + url + "?" + query_param
        else:
            request_url = self.host + self.prefix + url

        r = requests.request('GET', request_url, headers=headers)
        return r.json()
    

if __name__ == "__main__":
    pass

