# bot.py

import cfg
import socket
import time
import re

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

# NETWORK FUNCTIONS #
def chat(sock, message):
    """
    sends a chat message to the server
    :param sock: the socket over which to send the message
    :param message: the message to be sent
    """
    sock.send("PRIVMSG {} :{}".format(cfg.CHAN, message).encode("utf-8"))
    print("sent: {}".format(message))

def ban(sock, user):
    """
    bans a user from the channel
    :param sock: the socket over which to send the ban command
    :param user: the user to be banned
    """
    chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=300):
    """
    times a user out for a specified period of time (default 5 mins)
    :param sock: the socket over which to send the timeout command
    :param user: the user to be timed out
    :param secs: the time which the user will be timed out
    """
    chat(sock, ".timeout {}".format(user))


s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)
        if message[0] == "!":
            #strip the "!" from the command
            command = message[1:]
            if command in cfg.COMM_PATT:
                if command == "discord\r\n":
                    chat(s, "https://discord.gg/tCuyGGY\r\n")
                elif command == "pb\r\n":
                    chat(s, "http://www.speedrun.com/user/alexh0we\r\n")
                elif command == "wr\r\n":
                    chat(s, "http://www.speedrun.com\r\n")
                elif command == "hello\r\n":
                    chat(s, "What's going good {}.\r\n".format(username))
                elif command == "metalgear\r\n":
                    chat(s, "Metal Gear is fucking awful\r\n")
            else:
                chat(s, "What are you even trying to say. Get out of here.\r\n")
    time.sleep(1 / cfg.RATE)