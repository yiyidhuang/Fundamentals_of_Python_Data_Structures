"""
File: linkedset.py
"""


from linkedbag import LinkedBag
from abstractset import AbstractSet


class LinkedSet(AbstractSet, LinkedBag):
    """An linked-based set implementation"""

    # Constructor method
    def __init__(self, sourceCollection=None):
        """Set the initial state of self, which includes the contents of
        sourceCollection, if it's present."""
        LinkedBag.__init__(self, sourceCollection)

    # Mutator method
    def add(self, item):
        """Adds item to self, avoid deplicate item."""
        # Check array memory here and increase it if necessary.
        if item not in self:
            LinkedBag.add(self, item)
