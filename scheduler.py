import schedule
import time

import client
import db
import price_util


def checkTokens():
    token_list = db.getTokens()
    for token in token_list:
        price_change = client.getDayPriceChange(token + "EUR")
        price_util.checkPriceChange(price_change, token)

def initScheduler():
    schedule.every(10).seconds.do(checkTokens)

