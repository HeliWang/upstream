class Solution(object):
    def findPeakElement(self, nums):
        """
        Assume there will always a peak element since we can imagine nums[-1] = nums[n] = -∞
        """
        l = 0
        r = len(nums)
        # [1, 2, 3, 1]
        #  l           r
        #        m
        #        r
        #     m
        #        l
        #
        # [1,2,1,6,4]
        #  l         r
        while l < r:
            mid = (l + r) // 2
            # find the first element i which with num[i] > num[i + 1]
            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
