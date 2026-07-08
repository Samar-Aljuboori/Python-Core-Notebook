"""
Geometry Helper Module
This module provides functions for basic geometric calculations.
"""

#  PI ---> (Variable inside module)
PI = 3.14159

def calculate_circle_area(radius):
    """Calculates the area of a circle given its radius."""
    if radius < 0:
        return "Radius cannot be negative"
    return PI * (radius ** 2)

def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    if length < 0 or width < 0:
        return "Dimensions cannot be negative"
    return length * width

def welcome_message():
    """A simple welcome message from the module."""
    return "Geometry Helper Module loaded successfully!"