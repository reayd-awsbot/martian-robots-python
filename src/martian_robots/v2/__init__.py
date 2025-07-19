# mars_simulator/__init__.py
"""
mars_simulator package
Exports core classes and functions for easy import.
"""

from .main import Grid, Robot, Simulator, process_lines

__all__ = [
    "Grid",
    "Robot",
    "Simulator",
    "process_lines",
]
