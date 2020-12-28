import numpy
from dataclasses import dataclass


def add(x: int, y: int) -> int:
    return x + y


def add_arrays(x: numpy.ndarray, y: numpy.ndarray) -> numpy.ndarray:
    return x + y


def add_lists(x: list[int], y: list[int]) -> list[int]:
    return x + y


@dataclass
class Location:
    x: float
    y: float
