"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

n and k are non-negative integers.
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        if n <= 2: return k ** n
        ways_diff_last_chars = k * (k - 1) * k
        ways_same_last_chars = k * (k - 1)
        for i in range(4, n + 1):
            ways_diff_last_chars_bk = ways_diff_last_chars
            ways_same_last_chars_bk = ways_same_last_chars
            ways_diff_last_chars = ways_diff_last_chars_bk * (k - 1) + ways_same_last_chars_bk * (k - 1)
            ways_same_last_chars = ways_diff_last_chars_bk
        return ways_diff_last_chars + ways_same_last_chars
