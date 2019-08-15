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
