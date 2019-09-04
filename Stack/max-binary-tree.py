"""
https://leetcode.com/problems/maximum-binary-tree/

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
本题其实是构建笛卡树（Cartesian tree， https://en.wikipedia.org/wiki/Cartesian_tree），
经典方法是用单调栈（单调递减栈）。我们堆栈里存放的树，只有左子树，没有右子树，且根节点最大。时间复杂度为O(n)。
如果新来一个数，比堆栈顶的树根的数小，则把这个数作为一个单独的节点压入堆栈。
否则，不断从堆栈里弹出树，新弹出的树以旧弹出的树为右子树，连接起来，直到目前堆栈顶的树根的数大于新来的数。
然后，弹出的那些数，已经形成了一个新的树，这个树作为新节点的左子树，把这个新树压入堆栈。
这样的堆栈是单调的，越靠近堆栈顶的数越小。最后还要按照（2）的方法，把所有树弹出来，每个旧树作为新树的右子树。
"""


class Solution(object):


    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []  # max -> min stack
        for num in nums:
            node = TreeNode(num)
            # what if 4 2 1 3
            #   4
            #       3
            #     2
            #       1
            if stack and stack[-1].val < num:
                last_node = None
                while stack and stack[-1].val < num:
                    last_node = stack.pop()
                node.left = last_node
            if stack and stack[-1].val > num:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


def constructMaximumBinaryTree(nums):
    stack = []
    for i in range(len(nums)):
        cur = TreeNode(nums[i])
        # [3,2,1,6,0,5]

        #        6
        #   3         5
        #     2     0
        #       1

        while stack and stack[-1].val < nums[i]:
            cur.left = stack.pop()
        if stack:
            stack[-1].right = cur
        stack.append(cur)
    return stack[0]
