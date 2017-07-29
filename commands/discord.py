#discord.py

def discord(channel):
    """
    chats the discord info of the channel
    :param channel: the channel in which the bot is chatting
    :return: the discord info or appropriate message
    """
    #returns alex's discord
    if channel == "#alexh0we":
        return "https://discord.gg/tCuyGGY"
    #returns my dumb joke
    elif channel == "#nic_how":
        return "hahaha nic doesn't have his own discord who do you think he is?"
    else:
        return "no discord info found"