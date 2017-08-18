import socket

class TwitchAssist:
    def connect(host, port, password, username, channel):
        irc=socket.socket()
        irc.connect((host, port))
        irc.send('PASS oath:' + password + ' \r\n')
        irc.send('NICK ' + username + ' \r\n')
        irc.send('JOIN #' + channel + ' \r\n')

    def disconnect():
        irc.close()

    def sendmsg(channel, message):
        irc.send('PRIVMSG #' + channel + ' ' + message + ' \r\n')
