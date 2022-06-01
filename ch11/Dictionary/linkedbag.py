"""
File: linkedbag.py
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous


class LinkedBag(object):
    def __init__(self, sourceCollection=None):
        self._items = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        return self._size

    def __str__(self):
        return self._size

    def __isEmpty(self):
        return len(self) == 0

    def __add__(self, other):
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if other is self:
            return True
        if type(self) != type(other) \
            or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.dta
            cursor = cursor.next

    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def clear(self):
        self._size = 0
        self._items = None

    def remove(self, item):
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next

        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        self._size -= 1
