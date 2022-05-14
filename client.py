import requests
import json

host = "https://api.binance.com/"


def getCurrentPrice(symbol):
    res = requests.get(host + "api/v3/avgPrice?symbol=" + symbol)
    json_response = json.loads(res.text)
    return float(json_response["price"])


def getDayPriceChange(symbol):
    res = requests.get(host + "api/v3/ticker/24hr?symbol=" + symbol)
    json_response = json.loads(res.text)
    return float(json_response["priceChangePercent"])
