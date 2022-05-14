import client
import db

if __name__ == '__main__':
    db.initDb()
#    db.addToken("BNB")
    a = db.getTokens()
    print(a)
