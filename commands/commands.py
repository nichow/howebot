# commands.py

from cfg import COMM_PATT

def commands():
    """
    lists the commands usable by the bot
    :return: every possible command except command
    """
    _ret = "I can do these things: "
    for command in COMM_PATT:
        if command != "commands\r\n":
            _ret += "!" + command.rstrip("\r\n")
            # the following conditional presumes that the last command in the list in the cfg.py file is not
            # the command command
            if command != COMM_PATT[len(COMM_PATT) - 1]:
                _ret += ", "
    return _ret + "\r\n"