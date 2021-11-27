# Sell all cryptocurrencies every 24 hours.
## 00:00, 12:00
import os 
import requests 
import utils.order as order
from utils.auth import headers
from utils.info import Info_getAssets

API_SERVER_URL = os.environ.get('SERVER_URL')
currency_list = ['BTC', 'ETH']
market_list = getMarketName(currency_list)

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

def sell():
    for i in market_list:
        sell_all(i)
    return