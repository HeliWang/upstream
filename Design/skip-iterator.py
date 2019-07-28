from collections import Counter

class SkipIterator:
    def __init__(self, it):
        self.it = it  # iterator
        self.it_cache = None
        self.cache = None
        self.count = Counter()

    def __next(self):
        if self.it_cache:
            v = self.it_cache
            self.it_cache = None
            return v
        return self.it.next()

    def __has_next(self):
        if self.it_cache: return True
        try:
            self.it_cache = next(self.it)
            return True
        except StopIteration:
            return False

    def has_next(self):
        if not self.cache:
            self.__reset_cache()
        return self.cache is not None

    def next(self):
        if not self.cache:
            self.__reset_cache()
        v = self.cache
        self.cache = None # Forget to set self.cache = None
        return v

    def __reset_cache(self):
        while self.cache is None:
            if not self.__has_next(): break
            v = self.__next()
            if self.count[v] > 0:
                self.count[v] -= 1
            else:
                self.cache = v

    def skip(self, num):
        """
        After calling skip()
        The iterator will skip next occurrence of the given element num
        """
        if num == self.cache:
            self.cache = None
        else:
            self.count[num] += 1

import unittest

class TestSkipIter(unittest.TestCase):
    def test_1(self):
        arr = [1, 2, 3, 4, 5, 6, 5, 6, 2, 3]
        skit = SkipIterator(iter(arr))
        assert skit.has_next() == True
        assert skit.next() == 1
        skit.skip(5)
        skit.skip(5)
        assert skit.next() == 2
        assert skit.has_next() == True
        assert skit.next() == 3
        assert skit.has_next() == True
        assert skit.next() == 4
        assert skit.has_next() == True
        assert skit.next() == 6
        assert skit.has_next() == True
        assert skit.next() == 6
        assert skit.has_next() == True
        assert skit.next() == 2
        assert skit.has_next() == True
        assert skit.next() == 3
        assert skit.has_next() == False
        assert skit.has_next() == False

    def test_2(self):
        arr = [1, 2, 3, 4, 5, 6, 5, 6, 2, 3]
        skit = SkipIterator(iter(arr))
        assert skit.has_next() == True
        skit.skip(1)
        assert skit.has_next() == True
        assert skit.next() == 2
        skit.skip(2)
        assert skit.has_next() == True
        assert skit.next() == 3
        skit.skip(6)
        assert skit.has_next() == True
        skit.skip(4)
        assert skit.has_next() == True
        skit.skip(5)
        assert skit.has_next() == True
        skit.skip(5)
        assert skit.has_next() == True
        assert skit.next() == 6
        assert skit.has_next() == True
        assert skit.next() == 3
        assert skit.has_next() == False

    def test_3(self):
        arr = []
        skit = SkipIterator(iter(arr))
        assert skit.has_next() == False
        skit.skip(1)
        assert skit.has_next() == False

    def test_4(self):
        arr = [1, 2, 3, 2, 1]
        skit = SkipIterator(iter(arr))
        assert skit.has_next() == True
        skit.skip(1)
        assert skit.has_next() == True
        skit.skip(1)
        assert skit.has_next() == True
        skit.skip(2)
        assert skit.has_next() == True
        skit.skip(2)
        assert skit.has_next() == True
        skit.skip(3)
        assert skit.has_next() == False
        assert skit.next() == None

unittest.main()