import functools


class SolutionBit:
    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @functools.lru_cache
    def bike_dfs(self, bikes_bitset, i):
        worker = self.workers[i]
        min_cost = sys.maxsize
        for bike_id in range(self.n):
            bike = self.bikes[bike_id]
            if bikes_bitset & (1 << bike_id):
                cost = self.manhattan(worker, bike)
                if i > 0:
                    cost += self.bike_dfs(bikes_bitset & (~(1 << bike_id)), i - 1)
                    # ~ to ~ Binary Ones Complement	It is unary and has the effect of 'flipping' bits.
                    # ^ Binary XOR	It copies the bit if it is set in one operand but not both.
                min_cost = min(min_cost, cost)
        return min_cost

    def assignBikes(self, workers, bikes):
        self.m = len(workers)
        self.n = len(bikes)
        self.workers = workers
        self.bikes = bikes
        bikes_bitset = (1 << self.n) - 1
        return self.bike_dfs(bikes_bitset, self.m - 1)


class SolutionMem:
    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @functools.lru_cache
    def bike_dfs(self, bikes_bitset, i):
        worker = self.workers[i]
        min_cost = sys.maxsize
        for bike_id in range(self.n):
            bike = self.bikes[bike_id]
            if bikes_bitset[bike_id]:
                cost = self.manhattan(worker, bike)
                if i > 0:
                    cost += self.bike_dfs(bikes_bitset[:bike_id] + (False,) + bikes_bitset[bike_id + 1:], i - 1)
                    # (1) is 1, but (1, ) is a tuple (1)
                min_cost = min(min_cost, cost)
        return min_cost

    def assignBikes(self, workers, bikes):
        self.m = len(workers)
        self.n = len(bikes)
        self.workers = workers
        self.bikes = bikes
        bikes_bitset = (True,) * self.n  # (True) = 1, (True, ) = tuple(True)
        return self.bike_dfs(bikes_bitset, self.m - 1)


import functools


class SolutionSubsetDP:
    class Solution:
        def manhattan(self, p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def assignBikes(self, workers, bikes):
            self.m = len(workers)
            self.n = len(bikes)
            self.workers = workers
            self.bikes = bikes
            cost_matrix = [[0] * (2 ** self.n) for _ in range(self.m)]
            # cost[i][j]: min cost to match workers[:i + 1] by the bitset j
            #    where k-th bit is 1 if bike k is available for the match
            for i in range(self.m):
                for j in range(2 ** self.n):
                    cost_matrix[i][j] = sys.maxsize
                    worker = self.workers[i]
                    for bike_id in range(self.n):
                        bike = self.bikes[bike_id]
                        if j & (1 << bike_id):
                            cost = self.manhattan(worker, bike)
                            if i > 0:
                                cost += cost_matrix[i - 1][j & (~(1 << bike_id))]
                            cost_matrix[i][j] = min(cost_matrix[i][j], cost)
            return min(cost_matrix[self.m - 1])
