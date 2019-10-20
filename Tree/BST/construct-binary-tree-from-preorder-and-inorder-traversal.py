# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        n = len(inorder)
        inorder_map = dict(zip(inorder, list(range(n))))
        if n == 0: return None
        def build_tree(inorder_min, inorder_max):
            if not preorder:
                return None
            if not inorder_min < inorder_map[preorder[0]] < inorder_max:
                return None
            node = TreeNode(preorder.pop(0))
            node.left  = build_tree(
                   inorder_min, min(inorder_max, inorder_map[node.val]))
            node.right = build_tree(
                   max(inorder_min, inorder_map[node.val]), inorder_max)
            return node
        return build_tree(-1, n)