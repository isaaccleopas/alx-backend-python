#!/usr/bin/env python3
"""Type-annotated function that takes a float multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float"""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
