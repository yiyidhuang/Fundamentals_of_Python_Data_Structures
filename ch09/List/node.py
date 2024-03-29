"""
File. node.py
"""


class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    """Represents a doubly linked node."""

    def __init__(self, data=None, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
