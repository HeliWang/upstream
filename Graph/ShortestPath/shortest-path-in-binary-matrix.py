class Solution:
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] or grid[m - 1][n - 1]:
            return -1
        queue = collections.deque()
        queue.append((0, 0, 1))
        grid[0][0] = 1
        dire = [-1, 0, 1, 0, -1, -1, 1, 1, -1]
        while queue:
            r, c, step = queue.popleft()
            if r == m - 1 and c == n - 1:
                return step
            for k in range(len(dire) - 1):
                nr = r + dire[k]
                nc = c + dire[k + 1]
                if 0 <= nr < m and 0 <= nc < n and not grid[nr][nc]:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, step + 1))
        return -1
