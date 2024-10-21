from enum import IntEnum, auto


class Layer(IntEnum):
    BACKGROUND = auto()
    OBSTACLE = auto()
    FLOOR = auto()
    PLAYER = auto()
    PLAYER2 = auto()
    UI = auto()
