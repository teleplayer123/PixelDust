import struct
import ctypes
from typing import NamedTuple


PIXEL_COLOR = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}

class RGBA32(NamedTuple):
    r: ctypes.c_uint8
    g: ctypes.c_uint8
    b: ctypes.c_uint8
    a: ctypes.c_uint8

