class Solution(object):
    def minKnightMoves(self, x: int, y: int) -> int:
        # let's do bfs
        # Because of the symmetry, we can just look into the first
        # quadrant and also push only positive coordinates to the queue
        # also look for positive x and y
        if x == 0 and y == 0:
            return 0
        return self.bfs(abs(x), abs(y))

    def bfs(self, x, y):
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        q = [(0, 0, 0)]
        visited = set()
        visited.add((0, 0))
        while len(q) > 0:
            i, j, dis = q.pop(0)
            for move in moves:
                a, b = i + move[0], j + move[1]
                if (a, b) not in visited and a >= 0 and b >= 0:
                    if a == x and b == y:
                        return dis + 1
                    q.append((a, b, dis + 1))
                    visited.add((a, b))
