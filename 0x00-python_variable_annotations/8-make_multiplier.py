#!/usr/bin/env python3
""" This module returns a function that multiplies a float by multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function make_multiplier that takes a
    float multiplier"""
    def Multiplier(x: float) -> float:
        return x * multiplier
    return Multiplier
