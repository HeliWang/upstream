"""
Exercise: Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
find the duplicate one.

Example 1: Input: [1,3,4,2,2] Output: 2
Example 2: Input: [3,1,3,4,2] Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

Option 1: O(n) + Modify each element of the array as a counter
nums[i] = original value of nums[i] + k * len(nums)
# k is the count of value (i + 1)

Option 2: binary search O(nlogn) solution
"""


class Solution:
    def countLE(self, nums, t):
        """
        return # of element <= t
        """
        return len(list(filter(lambda x: x <= t, nums)))

    def findDuplicate(self, nums: List[int]) -> int:
        """
        O(n * log(n)) algorithm, similar time complexity as sorting

        [1, 1, 1]
        [1, 1, 1]
        [1, 1, 2]
        [2, 1, 1, 3]
        [1, 1, 2, 3]
        [3, 2, 1, 1]
        [1, 1, 2, 3, 4]
        [1, 1, 3, 1, 4]
        [4, 4, 3, 4, 4]
        """
        l = 1
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            # the result number r is the first number
            #  with countLE(r) > r
            # e.g.
            # [1, 3, 3, 4, 2]
            # [1, 3, 3, 4, 3] # an extra 3 replaces 2
            # [1, 3, 3, 3, 2] # an extra 3 replaces 4
            # countLE(1) = 1 is not > 1
            # countLE(2) = 1 is not > 1
            # countLE(3) = 4 > 3
            if self.countLE(nums, mid) > mid:
                r = mid
            else:
                l = mid + 1
        return l
