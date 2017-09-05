from cfg import Config
import socket
import re

def main():
    str("starting")
    irc=socket.socket()
    irc.connect((Config.HOST, Config.PORT))
    irc.send('PASS {}\r\n'.format(Config.PASS).encode("utf-8"))
    irc.send('NICK {}\r\n'.format(Config.USER).encode("utf-8"))
    irc.send('JOIN #{}\r\n'.format(Config.CHAN).encode("utf-8"))
    print("Connected!")

    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

    while True:
        readmsg = irc.recv(1024).decode("utf-8").rstrip()
        if readmsg == "PING :tmi.twitch.tv\r\n":
            irc.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            user = re.search(r"\w+", readmsg).group(0)
            msg = CHAT_MSG.sub("", readmsg)
            print("User:" + user + " Message:" + msg)

if __name__ == '__main__':
    main()