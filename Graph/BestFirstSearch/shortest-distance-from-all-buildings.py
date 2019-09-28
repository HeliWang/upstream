class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return -1
        M = len(grid)
        N = len(grid[0])
        buildings = sum(val for line in grid for val in line if val == 1)
        hit = [[0] * N for i in range(M)]
        distSum = [[0] * N for i in range(M)]

        def BFS(start_x, start_y):
            visited = [[False] * N for k in range(M)]
            visited[start_x][start_y] = True
            count1 = 1
            queue = collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:  # empty land
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:  # building which you cannot pass through
                            count1 += 1
            # if a building cannot get into another building,
            # then it is also not possible to build such house
            return count1 == buildings

        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:  # Buildings
                    # For each building, calculate the distance to each empty land
                    if not BFS(x, y): return -1
        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j]
                    and hit[i][j] == buildings] or
                   [-1])  # or [-1] means [] or [-1]
