from flask import Flask,redirect, url_for, request, render_template,session
from pymongo import MongoClient
import os
from moonBot import moonBot


moonBotController = Flask(__name__)
moonBotController.secret_key = 'ether moon timestamp'
if 'MOONBOT_DB_1_PORT_27017_TCP_ADDR' in os.environ:
    client = MongoClient(os.environ['MOONBOT_DB_1_PORT_27017_TCP_ADDR'], 27017)
    db = client.moonDb


@moonBotController.route('/') # display all votes and trading pair tick if provided with keys 
def moonWatch():
    
    _votes = db.tododb.find()
    votes = [vote for vote in _votes]
    if session.has_key('keys') :
        keys = session['keys']
        bot = moonBot(1, keys['pair'], keys['apiKey'], keys['secret'])
        tradePair = [keys['pair'],bot.queryPairs()]
        return render_template('votes.html', votes=votes, tradePair=tradePair)
    return render_template('votes.html', votes=votes)

@moonBotController.route('/newVotes', methods=['POST'])
def postVotes():
    votes = {
        'votingPeriod' : request.form['voting_period'],
        'votingPair' : request.form['voting_pair'],
        'count' : request.form['voting_volume'],
        'processed' : request.form['processed'] #processed or not
    }
    db.tododb.insert_one(votes)
    return redirect(url_for('moonWatch'))

@moonBotController.route('/moonWatch', methods=['POST'])
def queryPair():
    keys = {
        'pair' : request.form['pair'], #voting pair
        'apiKey' : request.form['apiKey'], #voting volume
        'secret' : request.form['secret'] #processed or not
    }
    session['keys'] = keys
    return redirect(url_for('moonWatch'))

if __name__ == "__main__":
    moonBotController.run(host='0.0.0.0', debug=True)
