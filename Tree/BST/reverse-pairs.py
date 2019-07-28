#!/usr/bin/env python

'''
    493. Reverse-Pairs
    Design a data structure that can update and query
    for keys (may contain duplicate keys) in the tree that >= a given key
'''

class Node():
    def __init__(self, key):
        self.key    = key
        self.left   = None
        self.right  = None
        self.ge_count = 0
        # count of keys >= `self.key` in the tree

class BST(object):
    def __init__(self, lst):
        """
        Initializes an empty symbol table.
        """
        self.root = None
        sorted_unique_lst = sorted(list(set(lst)))
        self.construct(sorted_unique_lst, 0, len(sorted_unique_lst) - 1)

    def construct(self, lst, li, ri):
        """
        Use the template for divide & conquering a list
        :param lst: sorted\ unique lst
        :param li: left index inclusive
        :param ri: right index inclusive
        """
        if li > ri: return
        mid = (li + ri) // 2
        self.root = self.insert(self.root, lst[mid])
        self.construct(lst, li, mid - 1)
        self.construct(lst, mid + 1, ri)

    def insert(self, h, key):
        """
        :param h: Insert the key in the subtree rooted at h (head)
        :param key
        """
        if h == None:
            return Node(key)
        elif key < h.key:
            h.left = self.insert(h.left, key)
        elif key > h.key:
            h.right = self.insert(h.right, key)
        return h

    def count_ge(self, key): # search
        """
        :param key
        :return: count of the number of keys in the symbol table >= `key`
        """
        res = 0
        def count_rec(h):
            nonlocal res
            if h == None:
                return
            if key == h.key:
                res += h.ge_count
            elif key < h.key:
                res += h.ge_count
                count_rec(h.left)
            elif key > h.key:
                count_rec(h.right)
        count_rec(self.root)
        return res

    def inc_count(self, key):
        """
        :param key: increase the count of key by one
        # Not possible to have un-matched key
        """
        def inc_rec(h):
            if key == h.key:
                h.ge_count += 1
            elif key < h.key:
                inc_rec(h.left)
            elif key > h.key:
                inc_rec(h.right)
                h.ge_count += 1
        inc_rec(self.root)

class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tree = BST(nums)
        res = 0
        for num in nums:
            res += tree.count_ge(2 * num + 1)
            tree.inc_count(num)
        return res