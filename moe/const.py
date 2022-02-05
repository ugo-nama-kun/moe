from enum import Enum, auto


class Action(Enum):
    left = auto()
    right = auto()
    write = auto()
    delete = auto()