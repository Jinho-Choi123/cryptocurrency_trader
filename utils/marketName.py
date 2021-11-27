def getMarketName(currency_list):
    market_list = []
    for i in currency_list:
        if i == 'KRW':
            pass
        else:
            market_list.append('KRW-' + i)
    return market_list