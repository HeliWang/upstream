# Given a list of points, Find a rectangle with maximum area, the triangle should not contain another point.
import sys


def max_triangle(points):  # points = [(x, y)...]
    n = len(points)
    points.sort()  # sort by x, if x equal, sort by y
    max_area = 0
    for i in range(n):
        pd = set()  # point_dict: (x, y)
        y_range = []
        x_0 = points[i][0]
        y_0 = points[i][1]
        y1_min = sys.maxsize
        # the min y1 encountered by the j loop below for all y_1 > y_0
        for j in range(i + 1, n):
            x_1 = points[j][0]
            y_1 = points[j][1]
            pd.add(points[j])
            if x_1 == x_0 or y_1 <= y_0: continue
            if (x_0, y_1) in pd and (x_1, y_0) in pd and y_1 < y1_min:
                max_area = max(max_area, abs(y_1 - y_0) * (x_1 - x_0))
            y1_min = min(y1_min, y_1)
    return max_area
