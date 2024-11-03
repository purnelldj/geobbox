"""
geobbox
========

A python library for georeferenced bounding boxes.
"""

__version__ = "0.0.1"

from .geobbox import BoundingBox
from .utm import UTM

__all__ = ["BoundingBox", "UTM"]
