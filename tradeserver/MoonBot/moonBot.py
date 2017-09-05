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
    
    
    def __init__(self, period=None, pair=None,apiKey=None, secret=None, allowed_pair=None):
        '''
        
        @param period: time period between making api calls
        @param pair:
        @param apiKey:
        @param secret:
        @param allowed_pair: a set of pre defined allowed pairs, we should cross join this pair to the available list on polo
        '''
        
        if apiKey and secret:
            self.conn = poloniex(apiKey,secret)
            self.allowd_pair = allowed_pair.intersection(set(self.queryCurrentTicker().keys()))
                
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
    
    @staticmethod
    def reversePair(pair):
        _pair = pair.split('_')
        return _pair[1] + '_' + _pair[0]
    
    #add this to avoid stupid self trading pair 
    @staticmethod
    def isSelfPair(pair):
        _pair = pair.split('_')
        return _pair[1] == _pair[0]
    
    def isValidPair(self, pair):
        if moonBot.isSelfPair(pair):
            return False
        if pair in self.allowed_pair or moonBot.reversePair(pair) in self.allowed_pair:
            return True 
    
    def isReady(self):
        if self.conn:
            return True
        return False
        
    
    def moonWatch(self):
        while True:
            print "Current time : {:%Y-%m-%d %H:%M:%S}".format(datetime.now()) + "market : %s: %s" %(self.pair,self.queryPairs())
            time.sleep(int(self.period))