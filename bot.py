# bot.py

import cfg
import socket
import time
import re

CHAT_MSG = re.compile(r'^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :')

# NETWORK FUNCTIONS #
def chat(sock, message):
    """
    sends a chat message to the server
    :param sock: the socket over which to send the message
    :param message: the message to be sent
    :return: null
    """
    sock.send('PRIVMSG () :()'.format(cfg.CHAN, message))

def ban(sock, user):
    """
    bans a user from the channel
    :param sock: the socket over which to send the ban command
    :param user: the user to be banned
    :return: null
    """
    chat(sock, '.ban {}'.format(user))

def timeout(sock, user, secs=300):
    """
    times a user out for a specified period of time (default 5 mins)
    :param sock: the socket over which to send the timeout command
    :param user: the user to be timed out
    :param secs: the time which the user will be timed out
    :return: null
    """
    chat(sock, '.timeout {}'.format(user))


s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
s.send('PASS {}\r\n'.format(cfg.PASS).encode('utf-8'))
s.send('NICK {}\r\n'.format(cfg.NICK).encode('utf-8'))
s.send('JOIN {}\r\n'.format(cfg.CHAN).encode('utf-8'))

while True:
    response = s.recv(1024).decode('utf-8')
    if response == 'PING :tmi.twitch.tv\r\n':
        s.send('PONG :tmi.twitch.tv\r\n'.encode('utf-8'))
    else:
        username = re.search(r'\w+', response).group(0)
        message = CHAT_MSG.sub('', response)
        print(username + ': ' + response)
    time.sleep(1 / cfg.RATE)