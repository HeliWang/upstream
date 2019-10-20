class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
         None [] []

         3 [3] [3]

            3
             \
             20
        [3, 20] [20, 3]
                 j   i
            inorder_map[j] > inorder_map[i]

            3
           /
         20
        [20, 3] [20, 3]
                 ^
                 j   i
            inorder_map[j] < inorder_map[i]

            3
           / \
          9  20
            /  \
           15   7
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
                     ^
                     j  i
            inorder[j] < inorder[i]
            But if 9 is left subtree of 15,
              then 9 should also be in the left subtree of 20,
              then 9 should also be in the right subtree of 3
                 --> inorder_map[3] < inorder_map[9]

        go through postorder in reversed way:
             j i
        (1) j can be left child of i
        (2) j can be right child of i
        (3) j can be in another subtree

        Use recursion to simplify the codebase
        """
        n = len(inorder)
        inorder_map = dict(zip(inorder, list(range(n))))
        if n == 0: return None

        def build_tree(inorder_min, inorder_max):
            if not postorder:
                return None
            if not inorder_min < inorder_map[postorder[-1]] < inorder_max:
                return None
            node = TreeNode(postorder.pop())
            node.right = build_tree(
                max(inorder_min, inorder_map[node.val]), inorder_max)
            node.left = build_tree(
                inorder_min, min(inorder_max, inorder_map[node.val]))
            return node

        return build_tree(-1, n)