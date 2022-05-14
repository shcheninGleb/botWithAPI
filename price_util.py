import telegramm_bot


def checkPriceChange(price_change, symbol):
    if (price_change > 5) or (price_change < -5):
        telegramm_bot.sendMessage("цена изменилась для " + symbol + " на " + str(price_change))
