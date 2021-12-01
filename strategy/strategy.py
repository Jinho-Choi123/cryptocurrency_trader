import asyncio
from .buy.pricewatcher import buyer 
from .sell import sell


currency_list = ['ETH']
#invoke every 6 hours
async def strategy():
    await sell(currency_list)
    for currency in currency_list:
        buyer(currency)
    return 

if __name__ == "__main__":
    asyncio.run(strategy())

