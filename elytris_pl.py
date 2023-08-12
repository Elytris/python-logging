# File created by Elytris Robotics using Python 3.11 on August 11th 2023
# https://github.com/Elytris
# to use this file, place it in in your project directory and import elytris_pl

from colorama import Fore

accepted = [
    "success",
    "failure",
    "process",
    "warning",
    "info"
]

colors = {
    "success": Fore.LIGHTGREEN_EX,
    "failure": Fore.RED,
    "process": Fore.LIGHTMAGENTA_EX,
    "warning": Fore.LIGHTYELLOW_EX,
    "info": Fore.BLUE,
}

emblems = {
    "success": "+",
    "failure": "x",
    "process": "/",
    "warning": "!",
    "info": "i",
}

class NullValueInput(Exception):
    def __init__(self) -> None:
        super().__init__("'strin' value cannot be empty")

class TypeNotFound(Exception):
    def __init__(self, wrongtype) -> None:
        self.wrongtype = wrongtype
        self.message = f"The log type indexed does not exist '{self.wrongtype}'"
        super().__init__(self.message)
    pass

def emblem(strtype):
    return f"{Fore.RESET}[{colors[strtype]}{emblems[strtype]}{Fore.RESET}] "

def log(strin, strtype):
    if strin == "":
        raise NullValueInput
    try:
        print(emblem(strtype) + str(strin))
    except KeyError:
        raise TypeNotFound(strtype)

def test(strin = None):
    if strin != None:
        for i in accepted:
            print(emblem(i) + str(strin))
    else:
        for i in accepted:
            print(emblem(i) + "This is a test message")
