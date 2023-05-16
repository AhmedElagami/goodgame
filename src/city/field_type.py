from enum import Enum


class FieldType(Enum):
    GRASS = 1
    WATER = 2

    WATER_RIGHT = 3
    WATER_LEFT = 4
    WATER_UP = 5
    WATER_DOWN = 6

    WATER_CORNER_LEFT_UP = 7
    WATER_CORNER_LEFT_DOWN = 8
    WATER_CORNER_RIGHT_UP = 9
    WATER_CORNER_RIGHT_DOWN = 10

    WATER_IN_CORNER_LEFT_UP = 11
    WATER_IN_CORNER_LEFT_DOWN = 12
    WATER_IN_CORNER_RIGHT_UP = 13
    WATER_IN_CORNER_RIGHT_DOWN = 14