# uptime.py helper method

import twitch

def uptime():
    return "Alex has been live for " + twitch.get_uptime() + "\r\n"