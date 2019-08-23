import heapq
from collections import defaultdict


class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]  [city1, city2, cost]
        :rtype: int
        """
        mst_set = set()
        edge = defaultdict(list)
        cost_min_pq = list()  # (cost, (i, j))
        res = 0
        # build graph
        for connection in connections:
            i = connection[0] - 1
            j = connection[1] - 1
            cost = connection[2]
            edge[i].append((j, cost))
            edge[j].append((i, cost))

        # WHAT IF THERE IS NO MST!!!!!
        mst_set.add(0)
        for j, cost in edge[0]:
            heapq.heappush(cost_min_pq, (cost, (0, j)))

        while len(cost_min_pq) > 0:
            cost, e = heapq.heappop(cost_min_pq)
            i, j = e
            if i in mst_set and j in mst_set:
                continue

            res += cost

            k = i  # the vertex not in mst_set
            if i in mst_set: k = j
            mst_set.add(k)
            for pair in edge[k]:
                w, c = pair
                heapq.heappush(cost_min_pq, (c, (k, w)))

        if len(mst_set) != N:
            return -1
        else:
            return res
