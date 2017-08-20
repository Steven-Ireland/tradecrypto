'''
Created on Aug 20, 2017

@author: litao
'''

from poloniex import poloniex
from datetime import datetime
import time

class moonBot(object):
    '''
    the bot that trade a shitcoin to the moon
    '''
    def __init__(self, period, pair,apiKey, secret):
        self.conn = poloniex(apiKey,secret)
        self.period = period
        self.pair = pair
    
    def moonWatch(self):
        while True:
            currentTicker = self.conn.api_query("returnTicker")
            pricePair = currentTicker[self.pair]["last"]
            print "Current time : {:%Y-%m-%d %H:%M:%S}".format(datetime.now()) + "market : %s: %s" %(self.pair,pricePair)
            time.sleep(int(self.period))