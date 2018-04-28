# commands.py

comm_patt = ["commands\r\n",
             "discord\r\n",
             "pb\r\n",
             "wr\r\n",
             "uptime\r\n",
             "hello\r\n",
             "metalgear\r\n"]


def commands():
    """
    lists the commands usable by the bot
    :return: every possible command except command
    """
    _ret = "I can do these things: "
    for command in comm_patt:
        if command != "commands\r\n":
            _ret += "!" + command.rstrip("\r\n")
            # the following conditional presumes that the last command in the list is not the command command
            if command != comm_patt[len(comm_patt) - 1]:
                _ret += ", "
    return _ret + "\r\n"
