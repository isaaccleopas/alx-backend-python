#!/usr/bin/env python3
"""Type-annotated function that takes a str and an int/float as arguments"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple str and float"""
    return k, float(v ** 2)
