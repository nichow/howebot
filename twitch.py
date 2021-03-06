# twitch.py

import json
import datetime
from urllib import request as req
import os

CLIENT_ID = str(os.environ.get("CLID"))
CHANNEL = str(os.environ.get("CHAN")).lstrip('#')
URL = "https://api.twitch.tv/kraken/streams/" + \
            CHANNEL + "?client_id=" + CLIENT_ID


def get_channel_id():
    """
    gets the channel ID for the streaming channel
    :return:
    """
    try:
        res = req.urlopen(URL, None)
        data = json.load(res)
        channel_id = data["_id"]
    except:
        channel_id = 0
    return channel_id


def get_game():
    """
    get the game being played on stream
    :return: the game being played
    """
    res = req.urlopen(URL, None)
    data = json.load(res)
    if data["stream"] is not None:
        stream_data = data["stream"]
        return stream_data["game"]
    else:
        return None


def get_uptime():
    """
    gets how long the stream has been up
    :return: how long the stream has been up
    """
    format = "%Y-%m-%d %H:%M:%S"
    res = req.urlopen(URL, None)
    data = json.load(res)
    if data["stream"] is not None:
        start = str(data["stream"].get("created_at")).replace('T', ' ').replace('Z', '')
        start = datetime.datetime.strptime(start, format)
        delta = datetime.datetime.utcnow() - start
        return str(delta).split('.')[0]
    else:
        return None


def get_followers():
    """
    fetches the follower data
    :return: number of followers
    """
    res = req.urlopen(URL, None)
    data = json.load(res)
    stream_data = data["stream"]
    return stream_data["followers"]
