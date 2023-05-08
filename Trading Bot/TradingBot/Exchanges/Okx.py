import time
import datetime as dt
import hmac
import base64
import requests
from urllib.parse import urlencode



class Okx(object):
    def __init__(self, api_key=None, api_secret=None, passphrase = None, base_url = None):
        self.base_url = base_url or 'https://www.okx.com'
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase

    def get_time(self,):
        return dt.datetime.utcnow().isoformat()[:-3]+'Z'

    def signature(self, timestamp, method, request_path, body, secret_key):
        if str(body) == '{}' or str(body) == 'None':
            body = ''
        message = str(timestamp) + str.upper(method) + request_path + str(body)
        mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
        d = mac.digest()
        return base64.b64encode(d)

    # set request header
    def get_header(self,request='GET', endpoint='', body:dict=dict()):
        cur_time = self.get_time()
        header = dict()
        header['CONTENT-TYPE'] = 'application/json'
        header['OK-ACCESS-KEY'] = self.api_key
        header['OK-ACCESS-SIGN'] = self.signature(cur_time, request, endpoint , body, self.api_secret)
        header['OK-ACCESS-TIMESTAMP'] = str(cur_time)
        header['OK-ACCESS-PASSPHRASE'] = self.passphrase
        return header

    def send_signed_request(self, http_method, url_path, payload={}):
        '''
        See https://stackoverflow.com/questions/66486374/how-to-sign-an-okex-api-request
        '''

        url = self.base_url + url_path
        header = self.get_header(http_method, url_path, payload)
        print(url)
        # print(header)
        response= requests.get(url, headers=header)
        response.json()
        return response.json()

    # used for sending public data request
    def send_public_request(self, url_path, payload={}):
        query_string = urlencode(payload, True)
        url = self.base_url + url_path
        if query_string:
            url = url + '?' + query_string
        print("{}".format(url))
        response = requests.get(url)
        return response.json()
    
if __name__ == '__main__':

    pass

