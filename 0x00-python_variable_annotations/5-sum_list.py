#!/usr/bin/env python3
""" This module returns the sum as a float"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated function sum_list which takes a list input_list"""
    if not input_list:
        return 0
    else:
        return input_list[0] + sum_list(input_list[1:])
