# wr.py]

from twitch import get_game

def world_record():
    """
    the wr command refers the user to the speedrun database
    :return: a link to speedrun.com
    """
    game = get_game()
    if game == "Portal":
        return "http://www.speedrun.com/Portal#inbounds"
    elif game == "Half-Life":
        return "http://www.speedrun.com/hl1"
    else:
        "Uh... not sure. Find the game here: http://www.speedrun.com"