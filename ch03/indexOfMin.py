"""
indexOfMin.py
"""


def index_of_min(lyst):
    """Returns the index of the minimum item."""
    min_index = 0
    current_index = 1
    while current_index < len(lyst):
        if lyst[current_index] < lyst[min_index]:
            min_index = current_index
        current_index += 1
    return min_index
