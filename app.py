# app.py

import os
import socket
import time
import re

import commands.hello as hello
import commands.discord as discord
import commands.wr as wr
import commands.pb as pb
import commands.uptime as uptime
import commands.commands as commands

from dotenv import load_dotenv
from flask import Flask
app = Flask(__name__)
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
load_dotenv()


# NETWORK FUNCTIONS #
def chat(sock, message):
    """
    sends a chat message to the server
    :param sock: the socket over which to send the message
    :param message: the message to be sent
    """
    sock.send("PRIVMSG {} :{}".format(os.environ.get("CHAN"), message).encode("utf-8"))
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
    :param secs: the time which the user will be timed out; defaults to 300 seconds
    """
    chat(sock, ".timeout {}".format(user))


@app.route("/")
def main():
    s = socket.socket()
    s.connect((os.getenv("HOST"), int(os.getenv("PORT"))))
    pw = "PASS {}\r\n".format(os.getenv("PASS")).encode('utf-8')
    nick = "NICK {}\r\n".format(os.getenv("NICK")).encode('utf-8')
    chan = "JOIN {}\r\n".format(os.getenv("CHAN")).encode('utf-8')
    s.send(pw)
    s.send(nick)
    s.send(chan)

    while True:
        response = s.recv(1024).decode("utf-8")
        # if the bot is pinged by twitch it responds with its pong so it doesn't get timed out for inactivity
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            # fetch the username and
            # message from the response
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response)
            print(username + ": " + message)
            # if the response is a command, parse the command
            if message[0] == "!":
                # strip the "!" from the command
                command = message[1:]
                if command in commands.comm_patt:
                    if command == "discord\r\n":
                        chat(s, "@" + username + " " + discord.discord(os.environ.get("CHAN")) + "\r\n")
                    elif command == "pb\r\n":
                        chat(s, "@" + username + " " + pb.pb() + "\r\n")
                    elif command == "wr\r\n":
                        chat(s, "@" + username + " " + wr.world_record() + "\r\n")
                    elif command == "uptime\r\n":
                        chat(s, "@" + username + " " + uptime.uptime() + "\r\n")
                    elif command == "hello\r\n":
                        chat(s, hello.greet(username) + "\r\n")
                    elif command == "commands\r\n":
                        chat(s, commands.commands())
                    elif command == "metalgear\r\n":
                        chat(s, "Metal Gear is fucking awful\r\n")
                else:
                    chat(s,
                         "What are you even trying to say, {}. Get out of here. Try !commands next time.\r\n").format(
                        username)
        rate = 20 / 30
        time.sleep(1 / rate)


if __name__ == "__main__":
    app.run()
