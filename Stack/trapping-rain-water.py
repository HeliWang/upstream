# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):
        rain = 0
        stack = []  # stack of indexes, values on which are reverse sorted [high -> low]
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                j = stack.pop()
                if stack:
                    rain += (i - stack[-1] - 1) * (min(height[stack[-1]], h) - height[j])
            stack.append(i)
        return rain


"""
每次从两端的高度较小的一端移动，这样做的意义在于我们每次都是遍历最短的一个位置，
也就是根据木桶原理这里最可能漏水，还需要维护一个当前边界的最大值．这样如果如果某一个高度小于当前维护的边界最大值，那么这里就可以保存一些水．
"""


class Solution(object):
    def trap(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while l < r and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water


# https://leetcode.com/problems/trapping-rain-water-ii/
"""
二维的原理和一维的思路基本是一样的．在一维中我们只需从两个端点选一个即可，而在二维中可选的点就扩大成了整个矩形的边．
根据上一题知道我们同样每次应该先选取边界最小的高度，所以很自然的可以想到应该用优先队列来保存周围边界（小顶堆）．
在我们访问过了一个点之后要继续往矩形内部遍历，这样还需要保存一个点的位置．为了防止再次访问已经访问过的点还需要用一个数组来标记每个点的访问状态．

时间复杂度应该是O(m*n*log(m+n))．
"""

import heapq


class Solution(object):
    def check_cell_valid(self, x, y):
        return 0 <= x <= self.m - 1 and 0 <= y <= self.n - 1

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        self.m = m = len(heightMap)
        if m < 2: return 0
        self.n = n = len(heightMap[0])
        if n < 2: return 0
        pq = []  # a min pq of cells
        visited = set()
        for i in range(n):
            for x, y in [(0, i), (m - 1, i)]:
                pq.append((heightMap[x][y], x, y))
                visited.add((x, y))
        for i in range(m):
            for x, y in [(i, 0), (i, n - 1)]:
                pq.append((heightMap[x][y], x, y))
                visited.add((x, y))
        heapq.heapify(pq)
        water = 0
        while pq:
            h, x, y = heapq.heappop(pq)
            for delta in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                x_neighbour = x + delta[0]
                y_neighbour = y + delta[1]
                if not self.check_cell_valid(x_neighbour, y_neighbour): continue
                neighbour_val = heightMap[x_neighbour][y_neighbour]
                if (x_neighbour, y_neighbour) in visited:
                    continue
                visited.add((x_neighbour, y_neighbour))
                water += max(0, h - neighbour_val)
                heapq.heappush(pq, (max(h, neighbour_val), x_neighbour, y_neighbour))

        return water
