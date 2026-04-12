#!/usr/bin/env python3
"""ResulShafili"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this code returns square of v and string  like tuple"""
    return (k, v ** 2)
