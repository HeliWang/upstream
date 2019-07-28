#!/usr/bin/env python

"""
    248. Strobogrammatic Number III

    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

    Example:

    Input: low = "50", high = "100"
    Output: 3
    Explanation: 69, 88, and 96 are three strobogrammatic numbers.
"""

import unittest

class Solution(object):
    strobogrammatic_map = dict([('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')])
    def largest_strobogrammatic_num(self, n, prefix):
        """
        form the largest strobogrammatic number of length n based on prefix
        return string of the smallest number
        e.g. (3, "1") -> "101"
        """
        res = ["8"] * n
        for i in range(n // 2):
            res[i] = "9"
            res[n - 1 - i] = "6"
        for i in range(len(prefix)):
            res[i] = prefix[i]
            res[n - 1 - i] = Solution.strobogrammatic_map[prefix[i]]
        return "".join(res)

    def smallest_strobogrammatic_num(self, n, prefix):
        """
        form the smallest strobogrammatic number of length n based on prefix
        return string of the smallest number
        e.g. (3, "1") -> "101"
        """
        res = ["0"] * n
        if n != 1: # note for the case when n = 1
            res[0] = res[-1] = "1"
        for i in range(len(prefix)):
            res[i] = prefix[i]
            res[n - 1 - i] = Solution.strobogrammatic_map[prefix[i]]
        return "".join(res)

    def count(self, low, high, n, prefix):
        """
        count how many strobogrammatic numbers are:
          with # of digits = n
          with the specified prefix
          and in the range [low, high]
        """
        i = len(prefix)
        if len(low) == n and self.largest_strobogrammatic_num(n, prefix) < low:
            return 0
        if len(high) == n and self.smallest_strobogrammatic_num(n, prefix) > high:
            return 0
        if i * 2 == n or i * 2 - 1 == n:
            return 1
        res = 0
        if i * 2 + 1 == n:  # add a single digit
            for c in ['0', '1', '8']:
                res += self.count(low, high, n, prefix + c)
        else:  # add a number to form a surrounding pair
            for c in ['0', '1', '6', '8', '9']:
                if i == 0 and c == '0': continue
                res += self.count(low, high, n, prefix + c)
        return res

    def strobogrammaticInRange(self, low, high):
        """
        low: str
        high: str

        return the count of how many strobogrammatic numbers are
          in the range [low, high]

        strobogrammaticInRange(0, 1000) = 19:
          0, 1, 8,
          11, 69, 88, 96,
          101, 111, 181,
          609, 619, 689,
          808, 818, 888,
          906, 916, 986,
        """
        res = 0
        for l in range(len(low), len(high) + 1):
            res += self.count(low, high, l, "")
        return res

class TestSolution(unittest.TestCase):
   def test_1(self):
       s = Solution()
       assert s.smallest_strobogrammatic_num(1, "") == "0" # !
       assert s.smallest_strobogrammatic_num(2, "") == "11" # !
       assert s.smallest_strobogrammatic_num(2, "1") == "11"
       assert s.smallest_strobogrammatic_num(3, "1") == "101"
       assert s.smallest_strobogrammatic_num(5, "1") == "10001"
       assert s.largest_strobogrammatic_num(5, "1") == "19861"

   def test_2(self):
       s = Solution()
       assert s.count("0", "1000", 1, "") == 3
       assert s.count("0", "1000", 2, "") == 4
       assert s.count("0", "1000", 3, "") == 12
       assert s.count("0", "1000", 4, "") == 0

unittest.main()