""" Given a matrix with value in each cell, and find the path with minimum sum of values in that path.
Path should start from (0, 0) to (m - 1, n - 1) and in each move you can only go to right, bottom, bottom right.
e.g., [[1,3,5],
      [2,1,1],
      [1,1,1]]  => [1,1,1]
explanation: 1(0,0) -> 1(1,1) -> 1(2,2)

Follow up: given some points, you need to make sure the returned path is including these points
Assume there will be a path through the points
e.g., [[1,3,5],[2,1,1],[1,1,1]], points=[[0, 2]] => [1,3,5,1,1]
explanation: 1(0,0) -> 3(0,1) -> 5(0,2) -> 1(1,2) -> 1(2,2)
"""
import sys
import unittest


def min_sum_path(mtx, p0, p1):
    """
    :param mtx: Given Matrix
    :return: A path consists of matrix values from (x0, y0) to (x1, y1)
    """
    x0, y0 = p0[0], p0[1]
    x1, y1 = p1[0], p1[1]
    print(x0, y0, x1, y1)
    m = x1 - x0 + 1
    n = y1 - y0 + 1
    assert m > 0 and n > 0

    cost = [[sys.maxsize] * n for i in range(m)]
    cost[x0][y0] = 0
    # cost[i][j] is the min cost of the path from mtx[x0, y0] to mtx[i][j]

    pathTo = [[None] * n for i in range(m)]
    pathTo[x0][y0] = (x0, y0)
    # pathTo[i][j] is the index pair of last cell pointing to the cell mtx[i][j]

    for i in range(m):
        r = i + x0
        for j in range(n):
            c = j + y0
            for x, y in [(i - 1, j - 1), (i, j - 1), (i - 1, j)]:  ###!!!!!!!!
                if x > x1 or x < x0 or y > y1 or y < y0: continue
                cost_xy = cost[x][y] + mtx[r][c]  # i j or r c?
                if cost_xy >= cost[i][j]: continue
                cost[i][j] = cost_xy  # i j or r c?
                pathTo[i][j] = (x0 + x, y0 + y)  # i j or r c?
    # get path
    stack = []
    cur = (x1, y1)
    while cur != (x0, y0):
        stack.append(mtx[cur[0]][cur[1]])
        cur = pathTo[cur[0] - x0][cur[1] - y0]
    stack.append(mtx[x0][y0])
    return stack[::-1]


def min_sum_path_including_pts(mtx, points):
    assert mtx and mtx[0]
    m = len(mtx)
    n = len(mtx[0])
    points.sort()
    if not points or points[0] != (0, 0):
        points.insert(0, (0, 0))
    if points[-1] != (m - 1, n - 1):
        points.append((m - 1, n - 1))
    res_path = []
    for i, point in enumerate(points):
        if i == 0: continue
        last_point = points[i - 1]  # typo mtx -> points
        # print(last_point, point)
        sub_path = min_sum_path(mtx, last_point, point)
        if i == 1:
            res_path.extend(sub_path)
        else:
            res_path.extend(sub_path[1:])
    return res_path


class MinSumPathTest(unittest.TestCase):
    def test1(self):
        mtx1 = [[1, 3, 5], [2, 1, 1], [1, 1, 1]]
        min_sum_path(mtx1, 0, 0, 2, 2) == [1, 1, 1]

    def test2(self):
        mtx1 = [[1, 0, 10], [2, 1, 1]]
        min_sum_path(mtx1, 0, 0, 1, 2) == [1, 0, 1]

    def test3(self):
        mtx1 = [[1, 10, 0], [0, 11, 12], [1, 1, 1]]
        min_sum_path(mtx1, 0, 0, 2, 2) == [1, 0, 1, 1]

    def test4(self):
        mtx = [[1, 3, 5], [2, 100, 1], [2, 100, 1], [1, 1, 1]]
        assert (min_sum_path_including_pts(mtx, [(1, 1)]) == [1, 100, 1, 1])

    def test5(self):
        mtx = [[1, 3, 5], [2, 100, 1], [2, 100, 1], [1, 1, 1]]
        assert (min_sum_path_including_pts(mtx, [(3, 2)]) == [1, 2, 2, 1, 1])
