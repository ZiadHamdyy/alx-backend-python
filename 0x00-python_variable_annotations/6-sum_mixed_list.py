#!/usr/bin/env python3
""" This module returns the sum as a float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """type-annotated function sum_mixed_list which takes a list mxd_lst"""
    return sum(mxd_lst)
