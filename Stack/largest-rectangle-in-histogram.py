"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
given height = [2,1,5,6,2,3]. The largest rectangle  has area = 10 unit.
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""


def largestRectangleArea(self, height):
    """For any bar x, if it's in a rectangle of which the height is also the height of x,
     we know that every bar in the rectangle must be no shorter than x.
     Then the issue is to find the left and right boundary where the bars are shorter than x.

    According to the code, when a bar is popped out from the stack,
    we know it must be higher than the bar at position i,
    so bar[i] must be the right boundary (exclusive) of the rectangle,
    and the previous bar in the stack is the first one that is shorter
    than the popped one so it must be the left boundary (also exclusive).
    Then we find the rectangle.
    """
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
