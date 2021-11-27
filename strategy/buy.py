# 변동성 돌파전략에 따라 thereshold을 구하고, 
## thereshold을 넘는 시점에 코인을 산다.
### 한번 구매하면 팔때까지 다시 구매하지 않는다.
from utils.time import get_time, get_yesterday, get_date, add_hours, sub_hours
from utils.info import Info_Candle
from utils.marketName import getMarketName
from collections import deque

currency_list = ['BTC', 'ETH']
market_list = getMarketName(currency_list)
k = 0.5 # noise value 
deq = deque(maxlen=5)

def get_thereshold(market):
    yesterday = get_yesterday()
    candle = Info_Candle(market, yesterday, 1)
    price_var = candle[0]['high_price'] - candle[0]['low_price']
    thereshold = candle[0]['trade_price'] + price_var * k
    return thereshold

def buy(market):
    thereshold = get_thereshold(market)
    
        
