# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        stack = []
        res   = []
        node_to_expand = root
        while stack or node_to_expand:
            while node_to_expand:
                stack.append(n)
                n = n.left
            e = stack.pop()
            res.append(e.val)
            expand(e.right, stack)
        return res