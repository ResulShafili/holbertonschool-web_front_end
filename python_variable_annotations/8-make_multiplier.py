#!/usr/bin/env python3
"""ResulShafili"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """this function returns a function"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
