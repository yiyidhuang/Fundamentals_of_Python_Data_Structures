"""
File: linkedset.py
"""


from linkedbag import LinkedBag
from abstractset import AbstractSet


class LinkedSet(LinkedBag, AbstractSet):
    """A link-based set implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedBag.__init__(self, sourceCollection)

    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        if item not in self:
            LinkedBag.add(self, item)
