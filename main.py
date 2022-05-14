import time
import schedule
import client
import db
import scheduler
import telegramm_bot

if __name__ == '__main__':
    db.initDb()
    scheduler.initScheduler()
    while True:
        schedule.run_pending()
        time.sleep(1)


#shchtest_bot - адресс
#5346495359:AAEyqiTZHDA4BImeXKbIMwyLFxkW6M_LFyc