import time
import requests
import hashlib
from urllib.parse import urlencode
import hmac
import datetime
import json
import base64

# https://algotrading101.com/learn/gemini-api-guide/
# https://docs.gemini.com/rest-api/#private-api-invocation

class Gemini:

    def __init__(self, api_key=None, api_secret=None, base_url = 'https://api.gemini.com' ) -> None:
        self._api_key = api_key
        self._api_secret = api_secret
        self._BASE_URL = base_url


    def get_header(self, url_path, param):
        t = datetime.datetime.now()
        payload_nonce = time.time()
        payload =  {"request": f"{url_path}", "nonce": payload_nonce}
        for k,v in param.items():
            payload[k] = v
        encoded_payload = json.dumps(payload).encode()
        b64 = base64.b64encode(encoded_payload)
        signature = hmac.new(self._api_secret.encode(), b64, hashlib.sha384).hexdigest()

        request_headers = {
            'Content-Type': "text/plain",
            'Content-Length': "0",
            'X-GEMINI-APIKEY': self._api_key,
            'X-GEMINI-PAYLOAD': b64,
            'X-GEMINI-SIGNATURE': signature,
            'Cache-Control': "no-cache"
            }
        return request_headers
        
    def send_signed_request(self, method = 'POST', url_path = '', param = {}):
        url = self._BASE_URL + url_path

        headers = self.get_header(url_path, param)
        res = requests.post(url, headers=headers)
        return res.json()

    # used for sending public data request
    def send_public_request(self, url_path, param={}):
        value = [v for k,v in param.items()]
        url = self._BASE_URL + '/v1/'+ url_path + '/'.join(value)
        response = requests.get(url)
        return response.json()


if __name__ == '__main__':

    pass
