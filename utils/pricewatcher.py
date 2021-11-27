import asyncio
import websockets
import json
from .Ticker import Ticker

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
            print(f">> {data}")
            
def recv_ticker(market, deq):
    asyncio.run(recv(market, deq))