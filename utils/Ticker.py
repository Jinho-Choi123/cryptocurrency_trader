import datetime
from pytz import timezone
class Ticker:
    def __init__(self, code, timestamp, open, trade, high, low, volume):
        self.code = code
        self.timestamp = timestamp
        self.open = open
        self.trade = trade
        self.high = high
        self.low = low
        self.volume = volume

    @staticmethod
    def from_json(json):
        return Ticker(
            code=json['code'],
            timestamp = datetime.datetime.fromtimestamp(json['trade_timestamp']/1000, tz = timezone('UTC')),
            open=json['opening_price'],
            trade = json['trade_price'],
            high=json['high_price'],
            low=json['low_price'],
            volume=json['acc_trade_volume_24h']
        )


    def __repr__(self):
        return self.__str__()


    def __str__(self):
        return f'Ticker <code: {self.code}, timestamp: {self.timestamp.strftime("%Y-%m-%d %H:%M:%S")},'\
            f' open: {self.open}, trade: {self.trade}, high: {self.high}, low: {self.low}, volume: {self.volume}>'