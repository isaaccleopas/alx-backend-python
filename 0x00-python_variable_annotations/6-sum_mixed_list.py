#!/usr/bin/env python3
"""Type-annotated function which takes a list of ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of int and floats as float"""
    return float(sum(mxd_lst))
