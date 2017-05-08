from os import environ

import MySQLdb


class Lottery:
    def __init__(self):
        self.db = MySQLdb.connect(host=environ['LOTTERY_HOST'],
                                  user=environ['LOTTERY_USER'],
                                  passwd=environ['LOTTERY_PASSWORD'],
                                  db=environ['LOTTERY_DB'],
                                  port=int(environ['LOTTERY_PORT']))

    def __del__(self):
        self.db.close()

    def close(self):
        self.db.close()

    def getAllNumbers(self):
        c = self.db.cursor()
        query = 'SELECT b1, b2, b3, b4, b5, b6 FROM lottery;'
        c.execute(query)
        return c.fetchall()

    def getNumberAfter(self, date):
        c = self.db.cursor()
        c.execute("""SELECT b1, b2, b3, b4, b5, b6 FROM lottery WHERE d > %s"""
            , (date,))
        return c.fetchall()
