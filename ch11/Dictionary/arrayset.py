"""
File: arrayset.py
"""


from arraybag import ArrayBag
from abstractset import AbstractSet


class ArraySet(ArrayBag, AbstractSet):
    """An array-based implementation of a set"""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the contents
        of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    def add(self, item):
        """Add item to the set if it is not in the set."""
        if item not in self:
            ArrayBag.add(self, item)
