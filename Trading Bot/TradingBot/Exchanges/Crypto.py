import time
import requests
import hashlib
from urllib.parse import urlencode
import hmac

# https://www.youtube.com/watch?v=WxZR-GDEm6E
# https://exchange-docs.crypto.com/spot/index.html#introduction
# https://exchange-docs.crypto.com/exchange/v1/rest-ws/index.html?python#introduction


class Crypto:

    def __init__(self, api_key=None, api_secret=None, base_url = 'https://api.crypto.com/v2/', max_level = 3) -> None:
        self._api_key = api_key
        self._api_secret = api_secret
        self._BASE_URL = base_url
        self.MAX_LEVEL = max_level

    def get_param(self, url_path, param):
        req = {
            "api_key": self._api_key,
            "id":1,
            "method": url_path,
            "nonce": int(time.time() * 1000)
        }
        req['params'] = param
        req['sig'] = self.get_signature(req)

        return req

    def params_to_str(self, obj, level):
        if level >= self.MAX_LEVEL:
            return str(obj)

        return_str = ""
        for key in sorted(obj):
            return_str += key
            if obj[key] is None:
                return_str += 'null'
            elif isinstance(obj[key], list):
                for subObj in obj[key]:
                    return_str += params_to_str(subObj, ++level)
            else:
                return_str += str(obj[key])
        return return_str

    def get_signature(self, req):
        if "params" in req:
            param_str = self.params_to_str(req['params'], 0)
        payload_str = req['method'] + str(req['id']) + req['api_key'] + param_str + str(req['nonce'])

        sig = hmac.new(
            bytes(str(self._api_secret), 'utf-8'),
            msg=bytes(payload_str, 'utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

        return sig


    def send_signed_request(self, method = 'POST', url_path = '', param = {}) :
        query_string = urlencode(param, True)
        url = self._BASE_URL + url_path + '?' + query_string
        json = self.get_param(url_path, param)
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url, json=json, headers=headers)
        return res.json()

    # used for sending public data request
    def send_public_request(self, url_path, param={}):
        query_string = urlencode(param, True)
        url = self._BASE_URL + url_path
        if query_string:
            url = url + '?' + query_string
        response = requests.get(url)
        return response.json()


if __name__ == '__main__':

    pass
