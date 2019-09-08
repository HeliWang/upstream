"""
TreeSet Implementation using binary search (bisect)

Usage:
from treeset import TreeSet
ts = TreeSet([3,7,2,7,1,3])
print(ts)
>>> [1, 2, 3, 7]

ts.add(4)
print(ts)
>>> [1, 2, 3, 4, 7]

ts.remove(7)
print(ts)
>>> [1, 2, 3, 4]

ts.remove(5)
print(ts)
>>> [1, 2, 3, 4]

ts.addAll([3,4,5,6])
print(ts)
>>> [1, 2, 3, 4, 5, 6]

print(ts[0])
>>> 1

print(ts[-1])
>>> 6

print(1 in ts)
>>> True

print(100 in ts)
>>> False

for i in TreeSet([1,3,1]):
	print(i)
>>> 1
>>> 3
"""
import bisect


class TreeSet(object):
    """
    Binary-tree set like java Treeset.
    Duplicate elements will not be added.
    When added new element, TreeSet will be sorted automatically.
    """

    def __init__(self, elements):
        self._treeset = []
        self.addAll(elements)

    def addAll(self, elements):
        for element in elements:
            if element in self: continue
            self.add(element)

    def add(self, element):
        if element not in self:
            bisect.insort(self._treeset, element)

    def ceiling(self, e):
        index = bisect.bisect_right(self._treeset, e)
        if self[index - 1] == e:
            return e
        return self._treeset[bisect.bisect_right(self._treeset, e)]

    def floor(self, e):
        index = bisect.bisect_left(self._treeset, e)
        if self[index] == e:
            return e
        else:
            return self._treeset[bisect.bisect_left(self._treeset, e) - 1]

    def __getitem__(self, num):
        return self._treeset[num]

    def __len__(self):
        return len(self._treeset)

    def clear(self):
        """
        Delete all elements in TreeSet.
        """
        self._treeset = []

    def clone(self):
        """
        Return shallow copy of self.
        """
        return TreeSet(self._treeset)

    def remove(self, element):
        """
        Remove element if element in TreeSet.
        """
        try:
            self._treeset.remove(element)
        except ValueError:
            return False
        return True

    def __iter__(self):
        """
        Do ascending iteration for TreeSet
        """
        for element in self._treeset:
            yield element

    def pop(self, index):
        return self._treeset.pop(index)

    def __str__(self):
        return str(self._treeset)

    def __eq__(self, target):
        if isinstance(target, TreeSet):
            return self._treeset == target.treeset
        elif isinstance(target, list):
            return self._treeset == target

    def __contains__(self, e):
        """
        Fast attribution judgment by bisect
        """
        try:
            return e == self._treeset[bisect.bisect_left(self._treeset, e)]
        except:
            return False
