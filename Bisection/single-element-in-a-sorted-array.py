class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        # [0,1,1]
        # [0,1,1,3,3]
        # [0,1,1,3,3,5,5]

        # [1,1,2]
        # [1,1,3,3,5]
        # [1,1,3,3,5,5,7]
        while l < r:
            mid = (l + r) // 2
            if mid == l:
                return nums[mid]
            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if nums[mid - 1] == nums[mid] and (r - l - 1) // 2 % 2 == 0:
                r = mid - 1
            elif nums[mid] == nums[mid + 1] and (r - l - 1) // 2 % 2 == 1:
                r = mid
            elif nums[mid] == nums[mid + 1] and (r - l - 1) // 2 % 2 == 0:
                l = mid
            elif nums[mid - 1] == nums[mid] and (r - l - 1) // 2 % 2 == 1:
                l = mid + 1
