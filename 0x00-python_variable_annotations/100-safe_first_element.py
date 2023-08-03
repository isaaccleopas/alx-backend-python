#!/usr/bin/env python3
"""Augment the code with the correct duck-typed annotations"""
from typing import Union, Any, List, Tuple


def safe_first_element(lst: Union[List[Any], Tuple[Any, ...]]
                      ) -> Union[Any, None]:
    """Types of the elements of the input are not known"""
    if lst:
        return lst[0]
    else:
        return None
