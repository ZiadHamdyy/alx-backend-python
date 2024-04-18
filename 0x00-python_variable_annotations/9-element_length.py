#!/usr/bin/env python3
""" This module return values with the appropriate types"""

from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate function’s parameters"""
    return [(i, len(i)) for i in lst]
