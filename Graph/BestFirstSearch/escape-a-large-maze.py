class SolutionWrongVersion1:
    def dfs(self, cur, depth, delta_x, delta_y):
        if not 0 <= cur[0] < 10 ** 6:
            return False
        if not 0 <= cur[1] < 10 ** 6:
            return False
        if cur in self.blocked:
            return False
        if cur in self.visited:
            return False
        if depth >= len(blocked):
            return True
        if cur == self.target:
            return True
        self.visited.add(cur)
        return any([self.dfs((cur[0] + 1, cur[1]), depth + 1),
                    self.dfs((cur[0] - 1, cur[1]), depth + 1),
                    self.dfs((cur[0], cur[1] + 1), depth + 1),
                    self.dfs((cur[0], cur[1] - 1), depth + 1)])

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        self.blocked = set(map(tuple, blocked))
        self.visited = set()
        self.source, self.target = tuple(source), tuple(target)
        source_to_dest = self.dfs(tuple(self.source), 0)
        self.visited = set()
        self.source, self.target = self.target, self.source
        dest_to_source = self.dfs(tuple(self.target), 0)
        return source_to_dest and dest_to_source


class SolutionWrongVersion2:
    def dfs(self, cur, depth, delta_x, delta_y):
        if not 0 <= cur[0] < 10 ** 6:
            return False
        if not 0 <= cur[1] < 10 ** 6:
            return False
        if cur in self.blocked:
            return False
        if cur in self.visited:
            return False
        if depth >= len(self.blocked):
            return True
        if cur == self.target:
            return True
        self.visited.add(cur)
        return any([self.dfs((cur[0] + delta_x, cur[1]), depth + 1, delta_x, delta_y),
                    self.dfs((cur[0], cur[1] + delta_y), depth + 1, delta_x, delta_y)])

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        self.blocked = set(map(tuple, blocked))
        self.visited = set()
        self.source, self.target = tuple(source), tuple(target)
        source_to_dest = any([self.dfs(tuple(self.source), 0, 1, 1), self.dfs(tuple(self.source), 0, 1, -1),
                              self.dfs(tuple(self.source), 0, -1, 1), self.dfs(tuple(self.source), 0, -1, -1)])
        self.visited = set()
        self.source, self.target = self.target, self.source
        dest_to_source = any([self.dfs(tuple(self.target), 0, 1, 1), self.dfs(tuple(self.target), 0, 1, -1),
                              self.dfs(tuple(self.target), 0, -1, 1), self.dfs(tuple(self.target), 0, -1, -1)])
        return source_to_dest and dest_to_source


# correct version BFS
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked: return True
        blocked = set(map(tuple, blocked))

        def check(blocked, source, target):
            si, sj = source
            ti, tj = target
            level = 0
            q = collections.deque([(si, sj)])
            vis = set()
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if i == ti and j == tj: return True
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6 and (x, y) not in vis and (x, y) not in blocked:
                            vis.add((x, y))
                            q.append((x, y))
                level += 1
                if level == len(blocked): break
            else:
                return False
            return True

        return check(blocked, source, target) and check(blocked, target, source)


# correct version DFS
from bisect import bisect_right
from typing import List
from collections import defaultdict


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked_rows = defaultdict(list)
        bloked_cols = defaultdict(list)

        for row, col in sorted(blocked):
            blocked_rows[col].append(row)
            bloked_cols[row].append(col)

        target_col = target[1]
        target_row = target[0]

        visited = set()

        # directions
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        TOP = 3

        def dfs(row, col):
            if row == target_row and col == target_col:
                return True

            for direction in RIGHT, DOWN, LEFT, TOP:
                next_row = row
                next_col = col
                if direction == RIGHT:
                    i = bisect_right(bloked_cols[row], col)

                    next_blocked_col = float('inf')
                    if i < len(bloked_cols[row]):
                        next_blocked_col = bloked_cols[row][i]

                    next_col = min(next_blocked_col - 1, target_col)
                elif direction == LEFT:
                    i = bisect_right(bloked_cols[row], col) - 1

                    next_blocked_col = -1
                    if i >= 0:
                        next_blocked_col = bloked_cols[row][i]

                    next_col = min(next_blocked_col + 1, target_col)
                elif direction == DOWN:
                    i = bisect_right(blocked_rows[col], row)

                    next_blocked_row = float('inf')
                    if i < len(blocked_rows[col]):
                        next_blocked_row = blocked_rows[col][i]

                    next_row = min(next_blocked_row - 1, target_row)
                elif direction == TOP:
                    i = bisect_right(blocked_rows[col], row) - 1

                    next_blocked_row = -1
                    if i >= 0:
                        next_blocked_row = blocked_rows[col][i]

                    next_row = min(next_blocked_row + 1, target_row)

                key = (next_row, next_col)

                if key in visited:
                    continue

                visited.add(key)

                if dfs(next_row, next_col):
                    return True

            return False

        return dfs(source[0], source[1])
