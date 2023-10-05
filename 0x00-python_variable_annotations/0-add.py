#!/usr/bin/python3
"""
Write a type-annotated function add that 
takes a float a and a float b as arguments 
and returns their sum as a float.
"""

def add(a: float, b: float) -> float:
    """Adds two floating-point numbers and returns their sum.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of a and b as a floating-point number.
    """
    result = a + b
    return result
