"""
File: arraysortedset.py
"""

from arraysortedbag import ArraySortedBag
from abstractset import AbstractSet

class ArraySortedSet(ArraySortedBag, AbstractSet):
    """An array-based set implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArraySortedBag.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        if item not in self:
            ArraySortedBag.add(self, item)
