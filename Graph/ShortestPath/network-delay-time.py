import sys
from collections import defaultdict


# Bellman-Ford Algorithm

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        in_edges = defaultdict(list)  # in-edge map cityB: [(cityA, cost)] cityA->cityB
        for time in times:
            s, d, c = time
            in_edges[d - 1].append((s - 1, c))
        dp = [[sys.maxsize] * N for _ in range(N)]
        # dp[i][j] length of shortest path from vertex N to vertex j + 1 using <= i edges
        dp[0][K - 1] = 0
        for edge_l in range(1, N):
            for i in range(N):
                dp[edge_l][i] = dp[edge_l - 1][i]
                for in_vertex, cost in in_edges[i]:
                    dp[edge_l][i] = min(dp[edge_l][i], dp[edge_l - 1][in_vertex] + cost)
        if max(dp[N - 1]) == sys.maxsize: return -1
        return max(dp[N - 1])
