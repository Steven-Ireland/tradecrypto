from flask import Flask,redirect, url_for, request, render_template,session
from moonBot import moonBot
from moonBase import moonBase
import ast,json


moonController = Flask(__name__)
moonController.secret_key = 'ether moon timestamp'
moonBase = moonBase()
moonBotA = moonBot()


@moonController.route('/') # display all votes and trading pair tick if provided with keys 
def moonWatch():
    
    votes = moonBase.getAllVotes()
    
    if moonBotA.isReady():
        balances = moonBotA.queryBalance()
        tradePair = [moonBotA.pair,moonBotA.queryPairs()]
        return render_template('votes.html', votes=votes, tradePair=tradePair, balances=balances, botStatus='ready to moon')
    return render_template('votes.html', votes=votes, botStatus='waiting for launch')


@moonController.route('/newVotes', methods=['POST'])
def postVotes():
    votes = {
        'votingPeriod' : request.form['voting_period'],
        'votingPair' : request.form['voting_pair'],
        'count' : request.form['voting_volume'],
        'processed' : request.form['processed'] #processed or not
    }
    moonBase.insertVotes(votes)
    return redirect(url_for('moonWatch'))

@moonController.route('/moonWatch', methods=['POST'])
def queryPair():
    pair = {
        'pair' : request.form['pair'], #voting pair
    }
    session['pair'] = pair
    return redirect(url_for('moonWatch'))

@moonController.route('/setUpBot', methods=['POST'])
def setUpBot():
    keys = {
        'pair' : request.form['pair'], #voting pair
        'apiKey' : request.form['apiKey'], #voting volume
        'secret' : request.form['secret'] #processed or not
    }
    moonBotA = moonBot(1, keys['pair'], keys['apiKey'], keys['secret'])

if __name__ == "__main__":
    moonController.run(host='0.0.0.0', debug=True)
