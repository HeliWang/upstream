class IndexMinPQ(object):
    """
    Assume insert(key, priority), update_priority(key, new_priority), delete(key), delete_min()
    operations are all in O(log n) time complexity
    The contains(key), find(key) -> priority, get_min operations are in O(1)

    Implementation:
    # pq: an array representation of PQ tree, the tree head element is at pq[1], each array element is a key
    # pr: a map which is key -> priority
    # qp: reverse a key to an index to the pq array, a map which is key -> index in pq


    BIG NOTE: THE NUMBERS IN THE NEXT LEVEL OF PQ IS NOT NECESSARY
    TO BE LARGER THAN CURRENT LEVEL, SINCE there might be in different subtree.

    say
          1
      2       8 <- higher than next level of 3, 4
    3  4   10  11
    """

    def __init__(self):
        self.pq = [None]
        self.pr = {}
        self.qp = {}

    def __swim__(self, k):  # 游泳；漂浮
        """
        :param k: index of pq
        """
        while k // 2 > 0 and self.__less__(k, k // 2):
            self.__exch__(k, k // 2)
            k = k // 2

    def __sink__(self, k):  # 沉没
        assert k > 0
        while k * 2 < len(self.pq):
            j = k * 2
            if j < len(self.pq) - 1 and self.__less__(j + 1, j):
                j += 1  # we need to swap with the lowest child node
            if self.__less__(k, j): break
            self.__exch__(k, j)
            k = j  # not k = k * 2!!!

    def __less__(self, i, j):
        """
        :param i: index of pq
        :param j: index of pq
        :return: if the corresponding priority of the key on index i is less than
                    the priority of the key on index j
        """
        assert 0 < i < len(self.pq)
        assert 0 < j < len(self.pq)
        return self.pr[self.pq[i]] < self.pr[self.pq[j]]

    def __exch__(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def insert(self, key, priority):
        assert not self.contains(key)
        k = len(self.pq)
        self.pq.append(key)
        self.pr[key] = priority
        self.qp[key] = k
        self.__swim__(k)

    def contains(self, key):
        """
        :param key
        :return: True if the key is included in the MinPQ, False otherwise
        """
        return key in self.qp

    def get_priority(self, key):
        """
        :param key
        :return: priority of the key in the PQ
        """
        assert self.contains(key)
        return self.pr[key]

    def remove(self, key):
        assert self.contains(key)
        k = self.qp[key]
        self.__exch__(k, len(self.pq) - 1)
        del self.qp[key]
        del self.pr[key]
        self.pq.pop()
        # what if the item deleted was actually len(len(self.pq) - 1)
        if k == len(self.pq): return
        self.__sink__(k)
        # what if k was with even lower priority (in the same level or belong to different subtree)
        self.__swim__(k)

    def update(self, key, new_priority):
        self.pr[key] = new_priority
        k = self.qp[key]
        self.__sink__(k)
        self.__swim__(k)

    def min(self):
        """
        :return: the key with min priority
        """
        assert len(self.pq) > 0
        return self.pq[1]

    def delete_min(self):
        key = self.pq[1]
        self.remove(key)
        return key

    def size(self):
        return len(self.pq) - 1


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        Special Cases: entry points with the same x-axis but different heights!!!!
        [[1,2,1],[1,2,2],[1,2,3]]
        Special Cases: points with [0 entry, 2 leave, 10 height]  [2 entry, 12 leave, 10 height]
        aka [[0,2,3],[2,5,3]]
        """
        pq = IndexMinPQ()
        points = []
        for i, building in enumerate(buildings):
            points.append((building[0], 0, - building[2], i))
            points.append((building[1], 1, building[2], i))
        points.sort()
        print(points)
        results = []
        for point in points:
            x_axis, state, height, building_idx = point
            if state == 0:
                height = - height
                if not pq.size() or buildings[pq.min()][2] < height:
                    results.append((x_axis, height))
                pq.insert(building_idx, - height)
            else:
                if pq.size() and pq.min() == building_idx:
                    pq.remove(building_idx)
                    height_left = 0
                    if pq.size(): height_left = buildings[pq.min()][2]
                    if height_left == height: continue
                    results.append((x_axis, height_left))
                else:
                    pq.remove(building_idx)
        return results
