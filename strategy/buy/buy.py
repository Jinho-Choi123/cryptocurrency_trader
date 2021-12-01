# 변동성 돌파전략에 따라 thereshold을 구하고, 
## thereshold을 넘는 시점에 코인을 산다.
### 한번 구매하면 팔때까지 다시 구매하지 않는다.
from utils.utils import get_time, get_yesterday, get_date, add_hours, sub_hours
from utils.info import Info_Candle
from utils.utils import getMarketName
from utils.order import get_KRW, Order 

k = 0.5 # noise value 

def get_thereshold(market):
    yesterday = get_yesterday()
    candle = Info_Candle(market, yesterday, 1)
    price_var = candle[0]['high_price'] - candle[0]['low_price']
    thereshold = candle[0]['trade_price'] + price_var * k
    return thereshold

def buy(market, ticker):
    thereshold = get_thereshold(market)
    if ticker['trade_price'] > thereshold:
        # buy
        krw_assets = get_KRW()
        price = krw_assets/10
        Order(market, 'bid', None, price, 'price')
        return True 
    return False 
    