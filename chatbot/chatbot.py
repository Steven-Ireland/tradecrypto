import cfg
import utils
import socket
import thread
import re

def main():
    irc=socket.socket()
    irc.connect((cfg.HOST, cfg.PORT))
    irc.send('PASS {}\r\n'.format(cfg.PASS).encode("utf-8"))
    irc.send('NICK {}\r\n'.format(cfg.PASS).encode("utf-8"))
    irc.send('JOIN #{}\r\n'.format(cfg.PASS).encode("utf-8"))

    while True:
        readmsg = irc.recv(1024).decode("utf-8").rstrip()
        if readmsg == "PING :tmi.twtich.tv\r\n":
            irc.send("PONG :tmi.twtich.tv\r\n".encode("utf-8"))
        else
            user = re.search(r'(?<=\:)([0-9A-Za-z_]*?)(?=\!)', readmsg)
            chan = re.search(r'(?<=PRIVMSG #)([0-9A-Za-z_]*?)(?= )', readmsg)
            mesg = re.search(r'(?<= \:)([0-9A-Za-z ]*?)(?=$)', readmsg)
