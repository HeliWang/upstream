"""
Test Case 1:
[1, 100, -10,  2, 4]
[9,   7,   1,  2, 4]
Cost: 1 + 9 + 7 + 1 - 10 + 2 + 2 + 4 = 16
However, there is a negative cycle in the above matrix.
The edge between the node -10 and 1 is -10 and 1
The edge between -10 and 1 is bidirectional
Hence, it is a negative cycle, BF algorithm will
not work here since a node will be revisited once there is a negative cycle

Test Case 2:
[1, 2000, -3000]
[9,   7,  1000]
Dijkstra Algorithm will find the solution 1 + 9 + 7 + 1000 = 1017
For BF algorithm, there is a negative cycle 2000, -3000 and 1000, -3000,
  which can not guarantee a node visited only once
However, the optimal solution 1 + 2000 - 3000 + 1000 = 1

Test Case 3:
[1, 20,  -1,  2,  4]
[9,  7,  20,  2,  4]

"""
import sys


# Solution1: DFS
# Time Complexity: O(4 **（m * n) similar to permutation problem
class DFS:
    def traversal(self, matrix, i, j, path_cost, visited):
        m, n = len(matrix), len(matrix[0])
        path_cost += matrix[i][j]
        if (i, j) == (m - 1, n - 1):
            self.res = min(self.res, path_cost)
            return
        for delta in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_i = i + delta[0]
            new_j = j + delta[1]
            if not 0 <= new_i < m:
                continue
            if not 0 <= new_j < n:
                continue
            if (new_i, new_j) in visited:
                continue
            visited.add((new_i, new_j))
            self.traversal(matrix, new_i, new_j, path_cost, visited)
            visited.remove((new_i, new_j))

    def shortest_path_cost(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        self.res = sys.maxsize
        visited = set([(0, 0)])
        self.traversal(matrix, 0, 0, 0, visited)
        return self.res


# Test Cases
matrix1 = [[1, 100, -10, 2, 4], [9, 7, 1, 2, 4]]
matrix2 = [[1, 2000, -3000], [9, 7, 1000]]

sol1 = DFS()
assert (sol1.shortest_path_cost(matrix1) == 16)
assert (sol1.shortest_path_cost(matrix2) == 1)

"""
# Solution2: Bellman-Ford DP Approach
# Only works for input without negative cycle
# dist[i][j] = the shortest distance from (0, 0) to (i, j) within path length <= k
#    0 < k <= m * n

Test Case 1:
[1,   17,  -1]
[9,   7,   2]
Cost: 1 + 9 + 7 + 2 - 1 + 2 + 2 + 4 = 16
"""


class BFDP:
    def shortest_path_cost(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dist = [[sys.maxsize] * n for _ in range(m)]
        dist[0][0] = 0
        for k in range(m * n - 1):
            for i in range(m):
                for j in range(n):
                    for delta in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        new_i = i + delta[0]
                        new_j = j + delta[1]
                        if not 0 <= new_i < m:
                            continue
                        if not 0 <= new_j < n:
                            continue
                        dist[new_i][new_j] = min(dist[new_i][new_j], dist[i][j] + matrix[new_i][new_j])
        print(dist)
        return dist[m - 1][n - 1]


# Test Cases
# [1, 17, -1],
# [9, 7,  2]
matrix3 = [[1, 17, -1], [9, 7, 2]]

sol2 = BFDP()
# matrix1 cannot be handled here since there is a neg cycle -10 <-> 1 here
assert (sol2.shortest_path_cost(matrix3) == 18)
8
# assert (sol2.shortest_path_cost(matrix2) == 1)
