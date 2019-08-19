# Fast Weighted (Balanced) Union with Path Compression

class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        # size[i] = number of sites in tree rooted at i
        #   Note: not necessarily correct if i is not a root node
        self.count = n
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
        if self.size[i] < self.size[j]:
            # make smaller root point to larger one
            self.parent[i] = j
            self.size[j] += self.size[i]
        else:
            self.parent[j] = i
            self.size[i] += self.size[j]

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


import unittest


class UFTest(unittest.TestCase):
    def test1(self):
        uf = UnionFind(4)
        assert uf.find(2) == 2
        uf.union(1, 2)
        assert uf.find(1) == uf.find(2)

        assert uf.find(3) == 3
        uf.union(1, 3)
        assert uf.find(3) == 1 or uf.find(3) == 2
        uf.union(3, 0)
        assert uf.find(0) == 1 or uf.find(0) == 2


unittest.main()
