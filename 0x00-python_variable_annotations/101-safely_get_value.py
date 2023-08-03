#!/usr/bin/env python3
"""parameters and the return values, add type annotations to the function"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any,
                     default: T = None) -> Union[Any, T]:
    """Return dct"""
    if key in dct:
        return dct[key]
    else:
        return default
