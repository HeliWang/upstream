"""
TreeSet Implementation using binary search (bisect)

Same interface as https://docs.oracle.com/javase/7/docs/api/java/util/TreeSet.html
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

    def ceiling(self, e):  # ge
        """
        By convention, say ceiling(2.4) == 3, ceiling(3) == 3
        Returns the leftmost element in this set greater than or equal to the given element,
        or None if there is no such element.
        """
        index = bisect.bisect_right(self._treeset, e)
        # all numbers of self._treeset[index:] are > e
        # thus, index can out of bound (= len(self._treeset)), or self._treeset[index] > e
        if self[index - 1] == e:
            return e
        if index == len(self._treeset): return None
        return self._treeset[bisect.bisect_right(self._treeset, e)]

    def higher(self, e):  # gt
        """
        By convention, say higher(2.4) == 3, higher(3) == 4
        Returns the leftmost element in this set that strictly greater than the given element,
        or None if there is no such element.
        """
        index = bisect.bisect_right(self._treeset, e)
        # all numbers of self._treeset[index:] are > e
        # thus, index can out of bound (= len(self._treeset)), or self._treeset[index] > e
        if index == len(self._treeset): return None
        return self._treeset[bisect.bisect_right(self._treeset, e)]

    def floor(self, e):  # le
        """
        By convention, say floor(2.4) == 2, floor(2) == 2
        Returns the rightmost element in this set less than or equal to the given element,
        or None if there is no such element (the array contains only number > e, or the array is empty)
        """
        index = bisect.bisect_left(self._treeset, e)
        # all numbers of self._treeset[index:] are >= e,
        # thus, index can out of bound (= len(self._treeset)),
        #   or self._treeset[index] == e,
        #   or self._treeset[index] > e
        if self[index] == e:
            return e
        elif index:  # index > 0
            return self._treeset[index - 1]
        else:
            return None

    def lower(self, e):  # lt
        """
        By convention, say floor(2.4) == 2, floor(2) == 2
        Returns the rightmost element in this set less than or equal to the given element,
        or None if there is no such element (the array contains only number > e, or the array is empty)
        """
        index = bisect.bisect_left(self._treeset, e)
        # all numbers of self._treeset[index:] are >= e,
        # thus, index can out of bound (= len(self._treeset)),
        #   or self._treeset[index] == e,
        #   or self._treeset[index] > e
        if index:  # index > 0
            return self._treeset[index - 1]
        else:
            return None

    def first(self):
        """
        :return: the first (lowest) element currently in this set, or None if not exist
        """
        return self._treeset[0] if self._treeset else None

    def last(self):
        """
        :return: the last (highest) element currently in this set, or None if not exist
        """
        return self._treeset[-1] if self._treeset else None

    def pollfirst(self):
        """
        :return: Retrieves and removes the first (lowest) element, or returns null if this set is empty.
        """
        if not self._treeset: return None
        return self._treeset.pop(0)

    def pollLast(self):
        """
        :return: Retrieves and removes the last (highest) element, or returns null if this set is empty.
        """
        if not self._treeset: return None
        return self._treeset.pop(-1)

    def __contains__(self, e):
        """
        Return True if e is in the treeSet
        """
        i = bisect.bisect_left(self._treeset, e)  # i can be len(self._treeset) if there is no element >= e
        if i != len(self._treeset):
            return e == self._treeset[i]
        else:
            return False

    def contains(self, e):
        return self.__contains__(e)

    def remove(self, e):
        """
        Remove element if element in TreeSet.
        """
        i = bisect.bisect_left(self._treeset, e)  # i can be len(self._treeset) if there is no element >= e
        if i != len(self._treeset) and e == self._treeset[i]:
            self._treeset.pop(i)
            # linear time: self._treeset.remove(element)
            return True
        return False

    def select(self, k):
        """Return the key in the symbol table whose rank is k (same as indexing)
        rank = the number of keys in the symbol table strictly less than `key`
             = the number of elements (>=0) before key [key]
        """
        if k < len(self._treeset):
            return self._treeset[k]
        else:
            return None

    def rank(self, key):
        """Return the rank of the key
             = the number of keys in the symbol table strictly less than `key`
             = the number of elements (>=0) before key [key]
        """
        return bisect.bisect_left(self._treeset, key)

    def range(self, lo, hi):
        """Returns all keys in the symbol table in [lo, hi].
        """
        return self._treeset[bisect.bisect_left(self._treeset, lo): bisect.bisect_left(self._treeset, hi)]

    def rangeSize(self, lo, hi):
        """Returns the number of keys in the symbol table in [lo, hi].
        """
        return bisect.bisect_left(self._treeset, hi) - bisect.bisect_left(self._treeset, lo)

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

    def __iter__(self):
        """
        Do ascending iteration for TreeSet
        """
        for element in self._treeset:
            yield element

    def __str__(self):
        return str(self._treeset)

    def __eq__(self, target):
        if isinstance(target, TreeSet):
            return self._treeset == target.treeset
        elif isinstance(target, list):
            return self._treeset == target