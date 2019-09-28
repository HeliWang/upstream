class Solution:
    def __init__(self):
        self.precision = 1e-5 / 2

    def findMaxAverage(self, nums, k):
        lo = sum(nums) / len(nums)
        hi = max(nums) + self.precision
        # find a min average that greater than all the valid average
        while lo + self.precision < hi:
            mid = (lo + hi) / 2
            if self.isMaxAvgGE(nums, k, mid):
                lo = mid + self.precision
            else:
                hi = mid
        return lo - self.precision

    def isMaxAvgGE(self, nums, k, avg):
        """
        nums = [1, 12, -5, -6, 50, 3], k = 4
        check if there is any contiguous subarray whose length is greater than or equal to k
         is with an average greater than or equal to a given avg:

        deltas = [1 - avg, 12 - avg, -5 - avg, -6 - avg, 50 - avg, 3 - avg]
                                                ^
                             ^j-k               j
                    minimum_delta

        we want to check if
            (prefix_sum[j] - prefix_sum[m]) / (j - m) >= avg
            (prefix_sum[j] - prefix_sum[m]) >= avg * (j - m)
            (prefix_sum[j] - prefix_sum[m]) >= avg + avg + avg .... + avg (sum for j - m times)
            prefix_sum[j] = sum(nums[0: j])
            prefix_sum[m] = sum(nums[0: m])
            prefix_sum[j] - prefix_sum[m] = sum(nums[j : m])
            sum(nums[j : m]) >=  avg + avg + avg .... + avg
            (nums[j] - avg) + (nums[j + 1]- avg) + .... (nums[m] - avg) >= 0

        if deltas[j] - minimum_delta > 0:
        """
        # delta[i] = nums[i] - avg
        min_prev_delta_psum = 0  # prefix sum of delta[0] + ...  + delta[i - k]
        prev_delta_psum = 0  # the prefix sum of all delta[0] + ... + delta[i - k]
        delta_psum = 0
        for i, num in enumerate(nums):
            delta_psum += nums[i]
            delta_psum -= avg
            if i >= k:
                prev_delta_psum += nums[i - k]
                prev_delta_psum -= avg
                min_prev_delta_psum = min(prev_delta_psum, min_prev_delta_psum)
            if i >= k - 1 and delta_psum >= min_prev_delta_psum:
                return True
        return False


s = Solution()
print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
