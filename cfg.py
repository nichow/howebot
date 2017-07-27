# cfg.py
import sys

HOST = 'irc.twitch.tv'
PORT = 6667
NICK = 'howebot'    # nickname of the bot
PASS = sys.argv[1]  # the authentication token of the user
CHAN = sys.argv[2]  # the user's channel
RATE = (20 / 30)    # messages / second

BAN_PATT = []       # patterns which result in a ban

COMM_PATT = []      # patterns which result in a response from the bot