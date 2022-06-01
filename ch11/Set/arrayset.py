"""
File: arrayset.py
"""


from arraybag import ArrayBag
from abstractset import AbstractSet


class ArraySet(ArrayBag, AbstractSet):
    """An array-based set implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        if item not in self:
            ArrayBag.add(self, item)
