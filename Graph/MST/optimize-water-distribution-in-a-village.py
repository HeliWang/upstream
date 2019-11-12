class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        # size[i] = number of sites in tree rooted at i
        #   Note: not necessarily correct if i is not a root node
        self.x = n
        # number of components

    def union(self, i, j):
        """
        :param i: vertex
        :param j: vertex
        :return: union vertex i and j to be the same connected component
        """
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j: return
        self.count -= 1
        # self.parent[root_i] = root_j  may be unbalanced
        if self.size[root_i] < self.size[root_j]:
            # make smaller root point to larger one
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
            # Typo: self.size[j] += self.size[i]
        else:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

    def find(self, i):
        """
        :param i: vertex
        :return: find connected component id of the vertex i
        """
        # id [1, 1, 3, 3]
        r = i  # root
        while r != self.parent[r]:
            r = self.parent[r]
        # self.parent[i] = p simple compression

        # better compression:
        q = i
        while q != r:
            new_q = self.parent[q]
            self.parent[q] = r
            q = new_q
        return r

    def connected(self, i, j):
        """
        :return:
        """
        return self.find(i) == self.find(j)


class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int

        Kruskal's Algorithm based on Union-Find
        """
