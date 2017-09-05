'''
Created on Sep 4, 2017

@author: litao

'''
from pymongo import MongoClient
import os


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
            self.db.votes.create_index('votingPeriod',unique=True)
            self.setCurrentVotingPeriod()
        else:
            raise Exception('can not connect to db through Tcp port')
        
    def getCurrentVotingPeriod(self):
        _votes = self.db.votes.find({'processed':{'$eq':'0'}}).sort([('votingPeriod',-1)]).limit(1)
        for vote in _votes:
            return vote['votingPeriod']
        return '0'
    
    def setCurrentVotingPeriod(self):
        self.currentVotingPeriod = self.getCurrentVotingPeriod()
        
    def getAllVotes(self):
        return [vote for vote in self.db.votes.find()]
    
    def getLastVotes(self):
        _votes = self.db.votes.find({'processed':{'$eq':'0'}}).sort([('votingPeriod',-1)]).limit(1)
        for vote in _votes:
            return vote
        return None
        
        
    #for tracking purpose
    def updateLocalBalanceHistory(self): 
        return
    
    def getLastestLocalBalance(self):
        return
    
    #should only be use for test
    def insertVotes(self,votes):
        self.db.votes.insert_one(votes)
        
    
    
        