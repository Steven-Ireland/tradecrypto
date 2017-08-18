from twitch_assist import TwitchAssist

HOST = 'irc.chat.twitch.tv'
PORT = '6667'

PASSWORD = 'blah'
USERNAME = 'tradecryptobot'
CHANNEL = 'tradecrypto'

twist = TwitchAssist()

twist.connect(HOST, PORT, PASSWORD, USERNAME, CHANNEL)
