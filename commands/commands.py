# commands.py

from cfg import COMM_PATT

def commands():
    _ret = "I can do these things: "
    for command in COMM_PATT:
        if command != "commands\r\n":
            _ret += "!" + command.rstrip("\r\n")
            if command != COMM_PATT[len(COMM_PATT) - 1]:
                _ret += ", "
    return _ret + "\r\n"