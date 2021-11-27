import os 
import jwt 
import uuid
import hashlib
from urllib.parse import urlencode

import requests 
from auth import headers
API_SERVER_URL = os.environ.get('SERVER_URL')

def Info_getAssets():
    headers_ = headers()
    res = requests.get(API_SERVER_URL + '/v1/accounts', headers = headers_)
    return res.json()

def Info_getMarketList():
    headers_ = {"Accept": "application/json"}
    query = {
        'isDetails': False,
    }
    res = requests.request("GET", API_SERVER_URL + '/v1/market/all', params = query, headers = headers_)
    print(res.json())
    return res.json()

def Info_Candle(market, to, count):
    query = {
        'market': market,
        'to': to,
        'count': count,
    }

    headers_ = {"Accept": "application/json"}
    res = requests.request("GET", API_SERVER_URL + '/v1/candles/days/', params = query, headers = headers_)
    return res

if __name__ == '__main__':
    Info_getMarketList()