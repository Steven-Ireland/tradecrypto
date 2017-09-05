'''
Created on Sep 4, 2017

@author: litao

'''
from pymongo import MongoClient
import os
import pymongo


class moonBase(object):
    '''
    db manager
    '''

    def __init__(self):
        self.initDb()

    
    def initDb(self):
        if 'MOONBOT_DB_1_PORT_27017_TCP_ADDR' in os.environ:
            client = MongoClient(os.environ['MOONBOT_DB_1_PORT_27017_TCP_ADDR'], 27017)
            self.db = client.moonDb
            self.db.votes.create_index([('votingPeriod', pymongo.DESCENDING),('votingPair',pymongo.ASCENDING)],unique=True)
            self.setCurrentVotingPeriod()
        else:
            raise Exception('can not connect to db through Tcp port')
        
    def getCurrentVotingPeriodFromDb(self):
        _votes = self.db.votes.find({'processed':{'$eq':'0'}}).sort([('votingPeriod',-1)]).limit(1) #cursor 
        for vote in _votes:
            return vote['votingPeriod']
        return '0'
    
    def setCurrentVotingPeriod(self):
        self.currentVotingPeriod = self.getCurrentVotingPeriodFromDb()
        
    def getAllVotes(self):
        return [vote for vote in self.db.votes.find()]
    
    def getLastVotes(self):
        _votes = self.db.votes.find({'processed':{'$eq':'0'}}).sort([('votingPeriod',-1)])
        return [vote for vote in _votes]
        
        
    #for tracking purpose
    def updateLocalBalanceHistory(self): 
        return
    
    def getLastestLocalBalance(self):
        return
    
    def markPeriodProcessed(self, period):
        self.db.votes.update_one({'votingPeriod':period},{'$set':{'processed':'1'}},upsert=False)
        return
    
    #should only be use for test
    def insertVotes(self,votes):
        self.db.votes.insert_one(votes)
        
    
        
    
    
        