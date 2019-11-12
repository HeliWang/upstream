"""
https://leetcode.com/problems/triangle/

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

Example：

Given the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

import sys


# 1. Traversal
# O(2^{n}), 其中n为Triangle中的层数（122*2…）进去n次
class Solution(object):
    def traversal(self, triangle, x, y, path_sum):
        """
        :param x: the pos x to be visited
        :param y: the pos y to be visited
        :param path_sum: sum so far
        :return:
        """
        path_sum += triangle[x][y]
        if x == len(triangle) - 1:
            self.res = min(path_sum, self.res)
        else:
            self.traversal(triangle, x + 1, y, path_sum)
            self.traversal(triangle, x + 1, y + 1, path_sum)

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.res = sys.maxsize
        self.traversal(triangle, 0, 0, 0)
        return self.res


# Note: we cannot transform a traversal to a DP, since traversal contains state information - the call to the traversal
#   function is dependent the path_sum state - dependent to last call

# 2. Bottom-up Recursion
# Enter from the head(top) problem. Recursively get the answer from the next sub-problems.
#  Base is at tail (bottom of the matrix). Each sub-problem is built upon the smaller sub-problem to the bottom.

class Solution(object):
    def minTotal(self, triangle, x, y):
        """
        :return: the min of path sum from (x, y) to the reachable bottom (n - 1, ...)
        """
        if x == len(triangle) - 1:
            return triangle[x][y]
        l = self.minTotal(triangle, x + 1, y)
        r = self.minTotal(triangle, x + 1, y + 1)
        return min(triangle[x][y] + l, triangle[x][y] + r)

    def minimumTotal(self, triangle):
        return self.minTotal(triangle, 0, 0)


# 3. Bottom-up Recursion + Memorization
class Solution(object):
    def minTotal(self, triangle, x, y, cache):
        """
        :return: the min of path sum from (x, y) to the reachable bottom (n - 1, ...)
        """
        if x == len(triangle) - 1:
            return triangle[x][y]
        if (x, y) in cache:
            return cache[(x, y)]
        l = self.minTotal(triangle, x + 1, y, cache)
        r = self.minTotal(triangle, x + 1, y + 1, cache)
        cache[(x, y)] = min(triangle[x][y] + l, triangle[x][y] + r, cache)
        return cache[(x, y)]

    def minimumTotal(self, triangle):
        cache = {}
        return self.minTotal(triangle, 0, 0, cache)


# 4. Top-down Recursion (Highly Recommend)
# Enter from the tail(bottom) problem. Recursively get the answer from the previous subproblems.
#  Base is at head (top). Each sub-problem is built upon the smaller sub-problem to the top.

class Solution(object):
    def minTotal(self, triangle, x, y):
        """
        :return: the min of path sum from (0, 0) to (x, y)
        """
        if x == 0:
            return triangle[0][0]
        res = sys.maxsize
        if y < len(triangle[x - 1]):
            res = min(res, self.minTotal(triangle, x - 1, y))
        if y - 1 >= 0:
            res = min(res, self.minTotal(triangle, x - 1, y - 1))
        return res + triangle[x][y]

    def minimumTotal(self, triangle):
        return min([self.minTotal(triangle, len(triangle) - 1, i) for i in range(len(triangle[len(triangle) - 1]))])


# 5. Top-down Recursion + Memorization
# O(number of elements) = O(1 + 2 + 3 + ... + n) = O(n ** 2)
class Solution(object):
    def minTotal(self, triangle, x, y, cache):
        """
        :return: the min of path sum from (0, 0) to (x, y)
        """
        if x == 0:
            return triangle[0][0]
        if (x, y) in cache:
            return cache[(x, y)]
        res = sys.maxsize
        if y < len(triangle[x - 1]):
            res = min(res, self.minTotal(triangle, x - 1, y, cache))
        if y - 1 >= 0:
            res = min(res, self.minTotal(triangle, x - 1, y - 1, cache))
        cache[(x, y)] = res + triangle[x][y]
        return cache[(x, y)]

    def minimumTotal(self, triangle):
        cache = {}
        return min(
            [self.minTotal(triangle, len(triangle) - 1, i, cache) for i in range(len(triangle[len(triangle) - 1]))])


# 6. Bottom-up (the bottom of matrix) DP Version1: Gather Info
# Reuse the answer from sub-problem to avoid duplication (the DP state must be in DAG! If there is a cycle,
#  no DP can be formed)
class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        # dist[x][y] means the min distance from (x, y) to any reachable bottom of matrix (n - 1, ..)
        dist = [[sys.maxsize] * n for _ in range(n)]
        for i in range(len(triangle[n - 1])):
            dist[n - 1][i] = triangle[n - 1][i]
        for x in range(n - 2, -1, -1):
            for y in range(len(triangle[x])):
                dist[x][y] = min(triangle[x][y] + dist[x + 1][y], triangle[x][y] + dist[x + 1][y + 1])
        return dist[0][0]


# 7. Bottom-up DP Version2: Provide Info
class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        # dist[x][y] means the min distance from (x, y) to any reachable bottom of matrix (n - 1, ..)
        dist = [[sys.maxsize] * n for _ in range(n)]
        for i in range(len(triangle[n - 1])):
            dist[n - 1][i] = triangle[n - 1][i]
        for x in range(n - 1, 0, -1):
            for y in range(len(triangle[x])):
                if y < len(triangle[x - 1]):
                    dist[x - 1][y] = min(dist[x - 1][y], triangle[x - 1][y] + dist[x][y])
                if y >= 1:
                    dist[x - 1][y - 1] = min(dist[x - 1][y - 1], triangle[x - 1][y - 1] + dist[x][y])
        return dist[0][0]


# 8. Top-down DP Version1: Gather Info from previous states (Highly Recommend)
class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        # dist[x][y] means the min distance from (0, 0) to (x, y)
        dist = [[sys.maxsize] * n for _ in range(n)]
        dist[0][0] = triangle[0][0]
        for x in range(1, n):
            for y in range(len(triangle[x])):
                if y < len(triangle[x - 1]):
                    dist[x][y] = min(dist[x][y], triangle[x][y] + dist[x - 1][y])
                if y >= 1:
                    dist[x][y] = min(dist[x][y], triangle[x][y] + dist[x - 1][y - 1])
        return min(dist[n - 1])


# 9. Top-down DP Version2: Provide Info to next states
class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        # dist[x][y] means the min distance from (0, 0) to (x, y)
        dist = [[sys.maxsize] * n for _ in range(n)]
        dist[0][0] = triangle[0][0]
        for x in range(n - 1):
            for y in range(len(triangle[x])):
                dist[x + 1][y] = min(dist[x + 1][y], triangle[x + 1][y] + dist[x][y])
                dist[x + 1][y + 1] = min(dist[x + 1][y + 1], triangle[x + 1][y + 1] + dist[x][y])
        return min(dist[n - 1])
