#!/usr/bin/env python3
""" This module add type annotations to the function"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List[int] = []
    for item in lst:
        for _ in range(factor):
            zoomed_in.append(item)
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
