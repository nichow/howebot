# hello.py, the greeting command
# TODO: add a plethora of additional greeting options for funsies
# import random as r

def greet(username):
    """
    greets the specified user
    :param username: the user to be greeted
    :return: string containing the greeting
    """
    return "Hey hey hey, what's goin' good {}".format(username)