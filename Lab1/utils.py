"""Utility functions for mathematical operations.

This module contains helper functions for common calculations,
including checking if a number is a perfect square.
"""

def is_perfect_square(n):
    """Check if a number is a perfect square, i.e., a square of an integer.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    return n>=0 and int(n**0.5)**2 == n