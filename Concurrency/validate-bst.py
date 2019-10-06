import sys
import threading


# Use Thread to Speed up to log(n) - WRONG WAY
# WRONG! WRONG! WRONG!!!

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


threadLock = threading.Lock()
threads = []
result = True


class myThread(threading.Thread):
    def __init__(self, root, lower, upper):
        threading.Thread.__init__(self)
        self.root = root
        self.lower = lower
        self.upper = upper

    def run(self):
        if self.root == None:
            return
        threadLock.acquire()
        if self.root.val <= self.lower or self.root.val >= self.upper:
            global result
            result = False
            threadLock.release()
            return
        # Create new threads
        thread1 = myThread(self.root.left, self.lower, self.root.val)
        thread2 = myThread(self.root.right, self.root.val, self.upper)
        # Add threads to thread list
        threads.append(thread1)
        threads.append(thread2)
        # !!!!!!! WRONG, since when thread is added to threads,
        #      for t in threads:
        #         t.join()
        #   May has been executed
        threadLock.release()
        # Start new Threads
        thread1.start()
        thread2.start()


def isValidBST(root):
    global result
    threads.clear()
    result = True
    thread = myThread(root, -sys.maxsize, sys.maxsize)
    threads.append(thread)
    thread.start()
    # Wait for all threads to complete
    for t in threads:
        t.join()
    return result


test_node1 = TreeNode(1)
test_node2 = TreeNode(0)
test_node3 = TreeNode(2)
test_node1.left = test_node2
test_node1.right = test_node3
assert isValidBST(test_node1)


# Use Thread to Speed up to log(n) – Correct:
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys
import threading
from queue import Queue


class myThread(threading.Thread):
    def __init__(self, root, lower, upper, return_queue):
        threading.Thread.__init__(self)
        self.root = root
        self.lower = lower
        self.upper = upper
        self.return_queue = return_queue

    def run(self):
        if self.root == None:
            self.return_queue.put(True)
            return
        if self.root.val <= self.lower or self.root.val >= self.upper:
            self.return_queue.put(False)
            return
        # Create new threads
        queue1 = Queue()
        thread1 = myThread(self.root.left, self.lower, self.root.val, queue1)
        queue2 = Queue()
        thread2 = myThread(self.root.right, self.root.val, self.upper, queue2)
        thread1.start()
        thread2.start()
        thread1.join()  # wait both
        thread2.join()
        result1 = queue1.get()
        result2 = queue2.get()
        self.return_queue.put(True if result1 and result2 else False)


def isValidBST(root):
    queue_result = Queue()
    thread = myThread(root, -sys.maxsize, sys.maxsize, queue_result)
    thread.start()
    thread.join()  # wait to complete
    return queue_result.get()


test_node1 = TreeNode(1)
test_node2 = TreeNode(0)
test_node3 = TreeNode(1)
test_node1.left = test_node2
test_node1.right = test_node3
assert (not isValidBST(test_node1))


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
            2
           / \
          1   3
        stack = [(2, -max, max)]
        stack = [(3, 2, max), (1, -max, 2)]
        stack = [(3, 2, max), (None, -max, 1), (None, 1, max)]
        """
        stack = [(root, -sys.maxint, sys.maxint)]
        while stack:
            node, minv, maxv = stack.pop()
            if not node: continue
            if not minv < node.val < maxv: return False
            stack += (node.right, node.val, maxv), (node.left, minv, node.val)
        return True


class SolutionRec(object):
    """
       root, min_val, max_val
         2   - sys.maxint, sys.maxint
         1   - sys.maxint, 2
         3   2, sys.maxint
    """

    def isValid(self, root, min_val, max_val):
        if not root:
            return True
        if min_val < root.val < max_val:
            return all([self.isValid(root.left, min_val, root.val), self.isValid(root.right, root.val, max_val)])
        else:
            return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, - sys.maxint, sys.maxint)