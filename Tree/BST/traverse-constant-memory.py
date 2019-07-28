class Node:
    def __init__(self, n):
        self.val   = n
        self.left  = None
        self.right = None

class Solution:
    def __init__(self, root):
        self.root      = root
        self.last_node = None
        while root:
            self.last_node = root
            root = root.left
        self.sum       = self.last_node.val

    def get_next(self):
        """
        :return: False when finish all the nodes
        """
        node = self.root
        prev = None
        while node:
            prev = node
            if node.left == self.last_node:
                node = node.right
            elif node.right == self.last_node:
                self.last_node = node
                # check if it is the last one
                if node == self.root:
                    return False
                else:
                    node = self.root
            else:
                node = node.left
        self.last_node = prev
        if prev and (not prev.left) and (not prev.right):
            self.sum += prev.val
        return True

    def get_leaves_sum(self):
        while self.get_next():
            pass
        return self.sum

# Test
root = Node(1)
root.left      = Node(2);
root.right     = Node(3);
root.left.left = Node(4);

'''4 becomes left child of 2 
           1 
       /       \ 
      2          3 
    /   \       /  \ 
   4    None  None  None 
  /  \ 
None None'''

s = Solution(root)
print(s.get_leaves_sum()) # should be 4 + 3 == 7