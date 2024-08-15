#!/usr/bin/python3
"""Minimum operations questions"""


def minOperations(n: int) -> int:
    """Finds the minimum operations"""
    available_chars = 1
    pending_chars = n - 1
    copied_chars = 0
    ops = 0

    while (pending_chars > 0):
        if copied_chars and pending_chars % available_chars:
            ops += 1
        else:
            copied_chars = available_chars
            ops = ops + 2
        available_chars += copied_chars
        pending_chars -= copied_chars
    return ops
