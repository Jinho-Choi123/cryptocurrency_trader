import os 
import jwt 
import uuid
import hashlib
from urllib.parse import urlencode

import requests 
from auth import headers
API_SERVER_URL = os.environ.get('SERVER_URL')

def Order(market, side, volume, price, ord_type):
    query = {
        'market': market,
        'side': side,
        'volume': volume,
        'price': price,
        'ord_type': ord_type,
    }

    query_string = urlencode(query).encode()
    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()
    query_hash_alg = 'SHA-512'
    headers_ = headers(query_hash, query_hash_alg)
    res = requests.post(API_SERVER_URL + '/v1/orders', params = query, headers = headers_)
    return res.json()

def Order_Sell_All(market_):
    headers_ = headers()
    res = requests.get(API_SERVER_URL + '/v1/accounts', headers = headers_)
    print(res.json())
    for i in res.json():
        if i['currency'] == 'KRW':
            pass
        elif i['currency'] == market_:
            market = i['unit-currency'] + '-' + i['currency']
            Order(market, 'ask', i['balance'], None, 'market')
        else:
            pass
    return res.json()

def get_KRW():
    headers_ = headers()
    res = requests.get(API_SERVER_URL + '/v1/accounts', headers = headers_)
    for i in res.json():
        if i['currency'] == 'KRW':
            return i['balance']
    return 0

if __name__ == '__main__':
    Order_Sell_All()