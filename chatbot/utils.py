import socket
import cfg

def sendmsg(irc, message):
    irc.send('PRIVMSG #' + channel + ' ' + message + ' \r\n')
