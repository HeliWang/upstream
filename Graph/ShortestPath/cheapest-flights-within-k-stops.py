import sys
import heapq
from collections import defaultdict


# Bellman-Ford Algorithm

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        adj = defaultdict(list)  # out-edge map cityA -> [(cityB, cost)]
        for flight in flights:
            s, d, c = flight
            adj[s].append((d, c))

        # cost[]: min cost of each city so far starting from src
        costTo = [sys.maxsize] * n
        costTo[src] = 0
        # min pq: (cost of reaching Y from src,
        #          Y,
        #          # of midpoints from src to Y)
        pq = [(0, src, 0)]

        while len(pq):
            y_path_cost, y, num_stops = heapq.heappop(pq)
            if y == dst:
                return y_path_cost
            costTo[y] = y_path_cost
            for d, cost in adj[y]:
                d_path_cost = y_path_cost + cost
                if costTo[d] <= d_path_cost: continue
                if num_stops == K + 1: continue  # please notice the num stop should be <= allowed mid + 1
                heapq.heappush(pq, (d_path_cost, d, num_stops + 1))
        return -1


"""
# Test Cases:
# (1) What if there is no route from src to dst?
# (2) What if there is a route (ru t) from src to dst but more than K midpoints?
# (3) What if:
#     there is a route from src to dst less than K midpoints with C1 as cost
#     there is a route from src to dst more than K midpoints with C2 as cost
#     C2 < C1
# (4) Multiple routes from src to dst
# (5) The best route requires fly back and forward (make a circle)
"""
