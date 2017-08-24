#fight_rate.py

import datetime
utcnow = datetime.datetime.utcnow()

def rate(channel, game, rating):
  if channel == "#alexh0we":
    return "alex doesn't play the punch games"
  if channel == "#nic_how":
    return rating, utcnow
