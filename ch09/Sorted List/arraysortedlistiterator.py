"""
File: arraysortedlistiterator.py
"""


class ArraySortedListIterator(object):
    """Represents the list iterator for a sorted array list."""

    def __init__(self, backingStore):
        """Set the initial state of the list iterator."""
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()
        self._cursor = 0
        self._lastItemPos = -1
        self.first()

    def first(self):
        """Resets the cursor to the beginning of the backing store."""
        self._cursor = 0
        self._lastItemPos = -1

    def last(self):
        """Moves the cursor to the end of the backing store."""
        self._cursor = len(self._backingStore)
        self._lastItemPos = -1

    def hasNext(self):
        """Return True if the iterator has a next item or False otherwise."""
        return self._cursor < len(self._backingStore)

    def next(self):
        """Precondition: hasNext returns True.
        The list has not been modified except by this iterators' mutator.
        Returns the current item and advances the cursor to the next item."""
        if not self.hasNext():
            raise ValueError("No next item in list iterator.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store.")
        self._lastItemPos = self._cursor
        self._cursor += 1
        return self._backingStore[self._lastItemPos]

    def hasPrevious(self):
        """Return True if the iterator has a previous item or False otherwise."""
        return self._cursor > 0

    def previous(self):
        """Precondition: hasPrevious returns True. The list has not been modified except
        by this iterators' mutator."""
        if not self.hasPrevious():
            raise ValueError("No previous item in list iterator.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store.")
        self._cursor -= 1
        self._lastItemPos = self._cursor
        return self._backingStore[self._lastItemPos]

    def remove(self):
        """Precondition: the current position is defined. The list has not been modified
        except by this iterators' mutator."""
        if self._lastItemPos == -1:
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        self._backingStore.pop(self._lastItemPos)
        # If the item removed was obtained via next, move cursor back
        if self._lastItemPos < self._cursor:
            self._cursor -= 1
        self._modCount += 1
        self._lastItemPos = -1
