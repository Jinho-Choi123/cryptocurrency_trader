# Sell all cryptocurrencies every 24 hours.
## 00:00, 12:00
import os 
import requests 
import utils.order as order
from utils.auth import headers
from utils.info import Info_getAssets
from utils.utils import getMarketName

API_SERVER_URL = os.environ.get('SERVER_URL')

## market_ is ETH, MLK, BTC... unit-currency is always KRW
def sell_all(market_):
    headers_ = headers()
    assets = Info_getAssets()
    for i in assets:
        if i['currency'] == 'KRW':
            pass
        elif i['currency'] == market_:
            market = i['unit-currency'] + '-' + i['currency']
            order.Order(market, 'ask', i['balance'], None, 'market')

def sell(currency_list):
    for i in currency_list:
        sell_all(i)
    return