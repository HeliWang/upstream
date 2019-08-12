"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node
to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if not node: return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.res = max(self.res, node.val, max(l, r) + node.val, l + r + node.val)
        return max(0, node.val, l + node.val, r + node.val)

    def maxPathSum(self, root):
        self.res = root.val
        self.dfs(root)
        return self.res


""" Wrong Version:
class Solution:
    def dfs(self, node):
        if not node: return 0
        self.res = max(self.res, node.val)
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.res = max(self.res, l + node.val)
        self.res = max(self.res, r + node.val)
        self.res = max(self.res, r + l + node.val)
        return max(l + node.val, r + node.val)

    def maxPathSum(self, root):
        self.res = root.val
        self.dfs(root)
        return self.res
"""
