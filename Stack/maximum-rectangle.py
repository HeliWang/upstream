"""
*(LC85) Maximal Rectangle*
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

*Example:*

*Input:*
[
  ["1","0","1","0","0"],
  ["1","0","*1*","*1*","*1*"],
  ["1","1","*1*","*1*","*1*"],
  ["1","0","0","1","0"]
]
*Output:* 6
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        heights = [0] * len(matrix[0])
        result = 0
        for row in matrix:
            for i, v in enumerate(row):
                if v == '0':
                    heights[i] = 0
                if v == '1':
                    heights[i] += 1
            result = max(result, self.largestRectangleArea(heights))
        return result

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        heights.append(0)
        for i, height in enumerate(heights):
            # mono stack [smallest -> largest]
            #   but storing index instead of (value, index)
            while stack and heights[stack[-1]] > height:
                idx = stack.pop()
                last_idx = -1
                if stack:
                    last_idx = stack[-1]
                result = max(result, (i - last_idx - 1) * heights[idx])
            stack.append(i)
        return result
