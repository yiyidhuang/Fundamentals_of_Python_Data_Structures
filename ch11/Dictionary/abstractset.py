"""
File: abstractset.py
"""


class AbstractSet(object):
    """Generic set method implementations."""

    def __or__(self, other):
        """Return the union of self and other."""
        return self + other

    def __and__(self, other):
        """Return the intersection of self and other."""
        intersection = type(self)()
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __sub__(self, other):
        """Return the difference of self and other."""
        difference = type(self)()
        for item in self:
            if item not in other:
                difference.add(item)
        return difference

    def issubet(self, other):
        """Returns True if self is a subset of other of False otherwise."""
        for item in self:
            if item not in other:
                return False
        return True
