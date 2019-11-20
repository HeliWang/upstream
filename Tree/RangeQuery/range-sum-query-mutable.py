class rangeTreeNode():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.value = 0  # the value when query range is not in [start, end]


class RangeTree():
    def __init__(self, nums):
        self.nums = nums

    def build(self, start, end):
        if not self.nums: return None
        new = rangeTreeNode(start, end)
        if start == end:
            new.value = self.nums[start]
        else:
            mid = (start + end) / 2
            new.left = self.build(start, mid)
            new.right = self.build(mid + 1, end)
            new.value = new.left.value + new.right.value
        return new

    def query(self, node, start, end):
        if not node or start > node.end or end < node.start:
            return 0  # the value when query range is not in [start, end]
        if start <= node.start and node.end <= end:
            return node.value
        else:
            left_return = self.query(node.left, start, end)
            right_return = self.query(node.right, start, end)
            return left_return + right_return

    def update(self, node, i, val):
        if not node:
            return 0  # the value when query range is not in [start, end]
        if node.start > i or node.end < i:
            return node.value  # the value when query range is not in [start, end]
        if node.start == node.end:
            node.value = val
        else:
            node.value = self.update(node.left, i, val) + self.update(node.right, i, val)
        return node.value


class NumArray(object):
    """
    Range Search Tree
    """

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = RangeTree(nums)
        self.root = self.tree.build(0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.tree.update(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.query(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
