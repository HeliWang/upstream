# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _new_id(self):
        # get an id from auto-increment
        self.cur_id += 1
        return self.cur_id

    def _get_tree_id(self, n):
        """Check if a tree with head n has been visited before
           by checking the signature of the tree
        If the tree is not visited,
           take a record of the tree, give a new id to the tree,
           and return the new id
        If the tree has been visited before,
           add the signature of the tree to self.res
           return the id in record

        A signature of a tree with head n:
           if n is not None,
             (_get_tree_id(n.left), _get_tree_id(n.right), n.val)
           if n is None,
             (None, None, None)

        n: the head of the input tree

        return the id of tree with head n
        """
        encoding = (None, None, None)
        if n:
            l_id = self._get_tree_id(n.left)
            r_id = self._get_tree_id(n.right)
            encoding = (l_id, r_id, n.val)
        if encoding in self.tree_signature_map:
            if n:
                self.res.add(encoding)
        else:
            self.tree_signature_map[encoding] = (self._new_id(), n)
        return self.tree_signature_map[encoding][0]

    def findDuplicateSubtrees(self, root):
        """Find dup subtree by encoding of the subtree
        an encoding of a subtree with node n as root is a triple (, n.val)
        """
        self.cur_id = 0
        self.tree_signature_map = {}  # (id_l, id_r, self.val) -> (id, node reference)
        self.res = set()
        self._get_tree_id(root)
        return [self.tree_signature_map[signature][1] for signature in self.res]