"""
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost]
  represents the cost to connect city1 and city2 together.
(A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities,
  there exists a path of connections (possibly of length 1) that
  connects those two cities together.  The cost is the sum of the
  connection costs used. If the task is impossible, return -1.
"""

import uf
import sys

class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]  [city1, city2, cost]
        :rtype: int
        """
        union_find = UnionFind(N)
        connections.sort(key=lambda x: x[2])
        res = 0
        for connection in connections:
            i = connection[0] - 1
            j = connection[1] - 1
            cost = connection[2]
            if union_find.find(i) == union_find.find(j): continue
            res += cost
            union_find.union(i, j)
        # WHAT IF THERE IS NO MST!!!!!
        cid = union_find.find(0)  # component id
        for i in range(N):
            if union_find.find(i) != cid: return -1
        return res
