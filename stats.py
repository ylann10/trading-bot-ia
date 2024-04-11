from binance.client import Client

def getStats(limit, toPredict=False):
    client = Client()
    result = []
    for data in client.get_historical_klines("ADAUSDT", "1d", limit=limit):
        obj = {}
        obj['start'] = data[0]
        obj['open'] = data[1]
        obj['high'] = data[2]
        obj['low'] = data[3]
        obj['close'] = data[4]
        obj['volume'] = data[5]
        obj['end'] = data[6]
        obj['quote_asset_volume'] = data[7]
        obj['trades'] = data[8]
        obj['taker_buy_base_asset_volume'] = data[9]
        obj['taker_buy_quote_asset_volume'] = data[10]
        result.append(obj)
    if toPredict:
        return getLastData(result)
    else:
        return getDataToFit(result)

def getDataToFit(dictList):
    data = {
        "x": [],
        "y": []
    }
    for i, obj in enumerate(dictList):
        l = []
        isLast = i == len(dictList) - 1
        l.append(obj['open'])
        l.append(obj['high'])
        l.append(obj['low'])
        l.append(obj['close'])
        l.append(obj['volume'])
        l.append(obj['trades'])
        if not isLast:
            data['x'].append(l)
            data['y'].append(dictList[i + 1]['close'])
    return data

def getLastData(dictList):
    data = []
    for i, obj in enumerate(dictList):
        l = []
        l.append(obj['open'])
        l.append(obj['high'])
        l.append(obj['low'])
        l.append(obj['close'])
        l.append(obj['volume'])
        l.append(obj['trades'])
        data.append(l)
    return data