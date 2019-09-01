# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
import heapq


class Solution:
    # [1,8,3,3,3]
    # 1+3  1+3+3 1+3+3+3 = 18 + 3 = 21
    # 1+3  3+3   1+3+3+3 = 17
    def connectSticks(self, sticks):
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            min1 = heapq.heappop(sticks)
            min2 = heapq.heappop(sticks)
            cost += (min1 + min2)
            heapq.heappush(sticks, min1 + min2)
        return cost


s = Solution()
s.connectSticks([2, 4, 3])
