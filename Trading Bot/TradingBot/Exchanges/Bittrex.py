import time
import urllib.parse
from typing import Optional, Dict, Any, List

from requests import Request, Session, Response
import hmac
import hashlib
import requests
from urllib.parse import urlencode

# https://algotrading101.com/learn/bittrex-api-guide/
# referece: https://stackoverflow.com/questions/62139890/bittrex-rest-api-v3-python-post-orders-invalid-content-hash


class Bittrex:

    def __init__(self, api_key=None, api_secret=None, subaccount_id=None, base_url = 'https://api.bittrex.com/v3') -> None:
        self._session = Session()
        self._api_key = api_key
        self._api_secret = api_secret
        self._subaccount_id = subaccount_id
        self._BASE_URL = base_url

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('GET', path, params=params)

    def _post(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('POST', path, json=params)

    def _delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request('DELETE', path, json=params)

    def _request(self, method: str, path: str, **kwargs) -> Any:
        request = Request(method, self._BASE_URL + path, **kwargs)
        self._sign_request(request)
        response = self._session.send(request.prepare())
        return response.json()


    
    def _sign_request(self, request: Request) -> None:
        ts = str(int(time.time() * 1000))
        prepared = request.prepare()
        content = ts + prepared.url + prepared.method
        if prepared.body:
            contentHash = hashlib.sha512(prepared.body).hexdigest()
        else:
            contentHash = hashlib.sha512(''.encode()).hexdigest()

        content += contentHash

        signature = hmac.new(self._api_secret.encode(), content.encode(), hashlib.sha512).hexdigest()
        request.headers['Api-Signature'] = signature
        request.headers['Api-Key'] = self._api_key
        request.headers['Api-Content-Hash'] = contentHash
        request.headers['Api-Timestamp'] = ts

        if self._subaccount_id:
            request.headers['Api-Subaccount-Id'] = urllib.parse.quote(self._subaccount_id)


    def send_signed_request(self, method: str, path: str, params) -> Any:

        if method == 'GET':
            return self._get(path, params)
        elif method == 'POST':
            return self._post(path, params)
        elif method == 'DELETE':
            return self._delete(path, params)

    def send_public_request(self, url_path, payload={}):
        url = self._BASE_URL + url_path
        response = requests.get(url)
        return response.json()

if __name__ == '__main__':
    pass
