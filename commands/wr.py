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
    elif game == 'Half-Life: Opposing Force':
        return "https://www.speedrun.com/op4"
    elif game == 'Gunman Chronicles':
        return "https://www.speedrun.com/gmc"
    else:
        "Uh... not sure. Find the game here: http://www.speedrun.com"
