"""
File: arraysortedlist.py
"""


from arrays import Array
from abstractlist import AbstractList
from arraysortedlistiterator import ArraySortedListIterator


class ArraySortedList(AbstractList):
    """An array-based sorted list implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the contents
        of sourceCollection, if it's present."""
        self._items = Array(ArraySortedList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection)

    # Accessor method
    def __iter__(self):
        """Support iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, i):
        """Precondition: 0<= i < len(self)
        Return the item at position i.
        Raises: IndexError"""

        if i < 0 or i >= len(self):
            raise IndexError("List out of range.")
        return self._items[i]

    def __contains__(self, item):
        position = self._binarySearch(item)
        if self._item[position] == item:
            return True
        else:
            return False

    def _binarySearch(self, item):
        """Search item in the array sorted list."""
        left = 0
        right = len(self) - 1
        mid = len(self)
        while left <= right:
            mid = (left + right) // 2
            if self._items[mid] == item:
                break
            if self._items[mid] > item:
                right = mid - 1
            else:
                left = mid + 1
        return mid

    def index(self, item):
        """Precondition: the item is in the list.
        Return the position of the item.
        Raise: ValueError if them isn't in the list."""
        position = self._binarySearch(item)
        if self._items[position] != item:
            raise ValueError(str(item) + " isn't in the list.")
        # find the first position if there is multiply items
        for i in range(position - 1, -1, -1):
            if self._items[i] != item:
                return i + 1
        # return the first place
        return 0

    # Mutator method
    def pop(self, i=None):
        """Precondition: 0 <= i < len(self).
        Remove and return item at position i. If i is None, i is given a default of len(self) - 1
        Raise: IndexError."""
        if i is None:
            i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range.")
        item = self._item[i]
        for index in range(i, len(self) - 1):
            self._items[index] = self._items[index + 1]
        self._items[len(self) - 1] = None
        self._size -= 1
        self.incModCount()
        # Resize array in necessary
        self._shrinkArray()
        return item

    def add(self, item):
        """Add the item to the proper position of the list."""
        # Resize the array if necessary.
        self._growArray()
        # Find the position by binary search
        position = self._binarySearch(item)
        flag = True
        if position < len(self) and self._items[position] != item:
            if item > self._items[position]:
                for i in range(position + 1, len(self)):
                    if item <= self._items[i]:
                        position = i
                        flag = False
                        break
                if flag:
                    position = len(self)
            else:
                for i in range(position - 1, -1, -1):
                    if item >= self._items[i]:
                        position = i + 1
                        flag = False
                        break
                if flag:
                    position = 0
        # Insert item at the proper position.
        if position < len(self):
            for index in range(len(self), position, -1):
                self._items[index] = self._items[index - 1]
        self._items[position] = item
        self._size += 1
        self.incModCount()

    def clear(self):
        """Clear the array list."""
        self._items = Array(ArraySortedList.DEFAULT_CAPACITY)
        self._size = 0
        self.incModCount()

    def listIterator(self):
        """Returns a list iterator."""
        return ArraySortedListIterator(self)

    def _growArray(self):
        """Grow the capactiy of the array if necessary"""
        physicalSize = len(self._items)
        if len(self) >= physicalSize:
            temp = Array(physicalSize * 2)
            index = 0
            for item in self:
                temp[index] = item
                index += 1
            self._items = temp

    def _shrinkArray(self):
        """Shrink the capacity of the array if necessary."""

        physicalSize = len(self._items)
        if len(self) <= physicalSize // 4 and physicalSize >= 2 * ArraySortedList.DEFAULT_CAPACITY:
            temp = Array(physicalSize // 2)
            index = 0
            for item in self:
                temp[index] = item
                index += 1
            self._items = temp
