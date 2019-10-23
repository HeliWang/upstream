class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
            3
             \
             20
        [3, 20], [20, 3]
            3
           /
         20
        [3, 20], [20, 3]

            3
             \
             20
            /  \
           15   7

               3
              /
             20
            /  \
           15   7
        [3, 20, 15, 7]
        [15, 7, 20, 3]

                3
              /   \
             20   15
                 /
                7
        [3, 20, 15, 7]
        [20, 7, 15, 3]

                3
              /   \
             20    7
            /
           15
        [3, 20, 15, 7]
        [15, 20, 7, 3]

            3
           / \
          9  20
            /  \
           15   7
        [3, 9, 20, 15, 7]
        [9, 15, 7, 20, 3]

        build([3, 9, 20, 15, 7], 5)
        node3 = Node(3)
        node3.left =
            build([9, 20, 15, 7], 4)
            node9
            node9.left = None
               build([20, 15, 7], 0)
            node9.right = None
               build([20, 15, 7], 0)
        node3.right =
            build([20, 15, 7], 4)
            node20
            node20.left =
              build([15, 7], 3)
              node15
            node20.right =
              build([7], 3)
              node7
        """
        n = len(post)
        postorder_map = dict(zip(post, list(range(n))))

        def build(seq, max_postorder):
            if not seq: return None
            if postorder_map[seq[0]] > max_postorder: return None
            v = seq.pop(0)
            node = TreeNode(v)
            node.left = build(seq, postorder_map[v])
            node.right = build(seq, postorder_map[v])
            return node

        return build(pre, n)