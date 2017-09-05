'''
Created on Aug 20, 2017

@author: litao
'''

from poloniex import poloniex
from datetime import datetime
import time
import json, ast

class moonBot(object):
    '''
    the bot that trade a shitcoin to the moon
    '''
    def __init__(self, period, pair,apiKey, secret):
        self.conn = poloniex(apiKey,secret)
        self.period = period
        self.pair = pair
    
    def queryPairs(self):
        currentTicker = self.conn.api_query("returnTicker")
        if self.pair in currentTicker:
            pricePair = currentTicker[self.pair]["last"]
            return pricePair
        return 'N/A'
    
    def queryCurrentTicker(self):
        return self.convertToStr(self.conn.api_query("returnTicker"))
    
    #scale to 8
    def queryBalance(self):
        return self.convertToStr(self.conn.returnBalances())
    
    def queryOpenOrder(self, currentPair=None):
        if currentPair is None:
            currentPair = self.pair
        return self.conn.returnOpenOrders(currentPair);
    
    def queryOrderBook(self, currentPair=None):
        if currentPair is None:
            currentPair = self.pair
        return self.conn.returnOrderBook(currentPair);
    
    def queryTradeHistory(self, currentPair=None):
        if currentPair is None:
            currentPair = self.pair
        return self.conn.returnTradeHistory(currentPair)
    
    #precisions of the amount?
    def buy(self, rate, amount, currentPair=None):
        if currentPair is None:
            currentPair = self.pair
        return self.conn.buy(currentPair, rate, amount)
    
    def sell(self, rate, amount, currentPair=None):
        if currentPair is None:
            currentPair = self.pair
        return self.conn.sell(currentPair, rate, amount)
    
    def cancel(self, orderNumber, currentPair=None):
        if currentPair is None:
            currentPair = self.pair
        self.conn.cancel(currentPair, orderNumber)
    
    def withdraw(self,amount, address,curentPair=None):
        if curentPair is None:
            currentPair = self.pair
        self.conn.withdraw(currentPair, amount, address)
        
    def convertToStr(self, inputs):
        return ast.literal_eval(json.dumps(inputs)) 
    
    def queryTargetBalance(self, currency):
        return self.queryBalance()[currency]
    
    
    def moonWatch(self):
        while True:
            print "Current time : {:%Y-%m-%d %H:%M:%S}".format(datetime.now()) + "market : %s: %s" %(self.pair,self.queryPairs())
            time.sleep(int(self.period))