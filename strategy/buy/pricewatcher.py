import asyncio
import websockets
import json
from utils.Ticker import Ticker
from buy import buy

async def recv(market):
    uri = 'wss://api.upbit.com/websocket/v1'
    market = market 
    async with websockets.connect(uri) as websocket:
        subscribe = [
            {"ticket": "test"},
            {
                "type": "ticker",
                "codes": [market],
                "isOnlyRealtime": True,
            },
            {"format": "DEFAULT",}
        ]

        subscribe_data = json.dumps(subscribe)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = Ticker.from_json(json.loads(data))
            #buy function here 
            trade_stat = await buy(market, data)
            if(trade_stat):
                print("Buy Success")
                break
            else:
                pass
        return 
            
# main buying function
def buyer(market):
    asyncio.run(recv(market))