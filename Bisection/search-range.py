class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def bisect_hi():
            """
            Return an index i so that a[i:] have e > x
            It is possible to have l == len(nums) if target > nums[-1]
            if target < nums[0]: l = 0
            """
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            return l

        def bisect_lo():
            """
            Return an index i so that a[i:] have e >= x
            It is possible to have l == len(nums) if target > nums[-1]
            if target < nums[0]: l = 0
            """
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            return l

        hi = bisect_hi()
        lo = bisect_lo()
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        return [lo, hi - 1]


import sys


class Solution(object):
    def binary_search(self, nums, target, lo, hi):
        if lo > hi: return
        mid = (lo + hi) // 2
        if nums[mid] == target:
            self.lo_res = min(self.lo_res, mid)
            self.hi_res = max(self.hi_res, mid)
            self.binary_search(nums, target, lo, mid - 1)
            self.binary_search(nums, target, mid + 1, hi)
        elif nums[mid] > target:
            self.binary_search(nums, target, lo, mid - 1)
        elif nums[mid] < target:
            self.binary_search(nums, target, mid + 1, hi)

    def searchRange(self, nums, target):
        self.lo_res = sys.maxsize
        self.hi_res = - sys.maxsize
        self.binary_search(nums, target, 0, len(nums) - 1)
        if self.lo_res == sys.maxsize: return [-1, -1]
        return [self.lo_res, self.hi_res]
