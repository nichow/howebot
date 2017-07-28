# hello.py, the greeting command

import random as r

def greet(username):
    """
    greets the specified user
    :param username: the user to be greeted
    :return: string containing the greeting
    """
    rand = int(r.Random(2 ** 10))
    if rand % 2 == 0:
        return "How's it hanging' {}".format(username)
    return "Hey hey hey, what's goin' good {}".format(username)