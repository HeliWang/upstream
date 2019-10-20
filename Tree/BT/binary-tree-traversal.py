class Solution:
    def inorderTraversal(self, root):
        # Build solution from base case:
        # (1) single node
        # (2) a simple tree with one root and two children
        #        3
        #   2       5
        # (3) complex tree
        #        3
        #   2       5
        # 0   1   8  10
        if not root: return []
        stack = []
        cur = root
        results = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            results.append(cur.val)
            cur = cur.right
        return results

    def inorderTraversalRecursion(self, root):
        if root is None:
            return []
        return self.inorderTraversalRecursion(root.left) + [root.val] \
               + self.inorderTraversalRecursion(root.right)

    def preorderTraversal(self, root):
        results = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            cur = stack.pop()
            results.append(cur.val)
            if cur.right:  # first add right to stack
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return results

    def postorderTraversal(self, root):
        # write your code here
        if not root: return []
        stack = [root]
        prev = None
        results = []
        while stack:
            cur = stack[-1]  # peek
            if not prev or prev.left == cur or prev.right == cur:
                # Traverse Down the tree
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
            elif cur.left == prev:
                if cur.right:
                    stack.append(cur.right)
            else:  # including the case where cur == prev and cur.right = prev
                results.append(cur.val)
                stack.pop()
            prev = cur
        return results

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
        """
        if not root: return []
        queue = deque()
        queue.append((0, root))
        level_nodes_map = defaultdict(list)  # VerticalOrder -> list of nodes
        while queue:
            level = list(queue)
            for vert_order, node in level:
                queue.popleft()
                level_nodes_map[vert_order].append(node.val)
                if node.left:  queue.append((vert_order - 1, node.left))
                if node.right: queue.append((vert_order + 1, node.right))
        sorted_level_nodes_map = sorted(list(level_nodes_map.items()))
        return list(map(lambda x: x[1], sorted_level_nodes_map))
