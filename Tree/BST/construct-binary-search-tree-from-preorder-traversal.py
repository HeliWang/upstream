class Solution:
    def helper(self, preorder, minv, maxv):
        if len(preorder) == 0:
            return None
        v = preorder[0]
        if minv < v < maxv:
            n = TreeNode(v)
            preorder.pop(0)
            n.left = self.helper(preorder, minv, v)
            n.right = self.helper(preorder, v, maxv)
            return n
        else:
            return None

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.helper(preorder, -sys.maxsize, sys.maxsize)