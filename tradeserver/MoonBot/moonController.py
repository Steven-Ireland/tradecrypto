from flask import Flask,redirect, url_for, request, render_template,session
from moonBot import moonBot
from moonBase import moonBase
import ast,json


moonBotController = Flask(__name__)
moonBotController.secret_key = 'ether moon timestamp'
moonBase = moonBase()


@moonBotController.route('/') # display all votes and trading pair tick if provided with keys 
def moonWatch():
    
    votes = moonBase.getAllVotes()
    
    if session.has_key('keys') :
        keys = ast.literal_eval(json.dumps(session['keys']))
        moonBotController.logger.info(keys)
        bot = moonBot(1, keys['pair'], keys['apiKey'], keys['secret'])
        balances = bot.queryBalance()
        tradePair = [keys['pair'],bot.queryPairs()]
        return render_template('votes.html', votes=votes, tradePair=tradePair, balances=balances)
    return render_template('votes.html', votes=votes)


@moonBotController.route('/newVotes', methods=['POST'])
def postVotes():
    votes = {
        'votingPeriod' : request.form['voting_period'],
        'votingPair' : request.form['voting_pair'],
        'count' : request.form['voting_volume'],
        'processed' : request.form['processed'] #processed or not
    }
    moonBase.insertVotes(votes)
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
