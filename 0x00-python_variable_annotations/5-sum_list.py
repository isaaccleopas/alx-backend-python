#!/usr/bin/env python3
"""Type-annotated function that takes a list of float arguement"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the float sum of float arguements"""
    return sum(input_list)
