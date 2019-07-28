# Stream of ints
# [1, 5, 3, 2] => (2 + 3) / 2 = 2.5
# [5, 3, 4, 2, 1] => 3

# Two Heaps
# int x
# Heap A
#  Max Heap
# heap B
#  Min Heap

import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def add(self, x):
        heapq.heappush(self.heap, - x)

    def peek(self):
        return - self.heap[0]

    def pop(self):
        return - heapq.heappop(self.heap)

class MinHeap():
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def add(self, x):
        heapq.heappush(self.heap, x)

    def peek(self):
        return self.heap[0]

    def pop(self):
        return heapq.heappop(self.heap)


class MedianFinder:
    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()

    def add_num(self, x):
        if self.max_heap.size() == 0 or self.max_heap.peek() >= x:
            self.max_heap.add(x)
        else:
            self.min_heap.add(x)
        self.balance_heaps()

    def balance_heaps(self):
        if self.max_heap.size() > self.min_heap.size() + 1:
            self.min_heap.add(self.max_heap.pop())
        elif self.min_heap.size() > self.max_heap.size():
            self.max_heap.add(self.min_heap.pop())

    def get_median(self):
        if self.max_heap.size() == 0:
            return None
        if self.max_heap.size() == self.min_heap.size():
            return (self.max_heap.peek() + self.min_heap.peek()) / 2
        else:
            return self.max_heap.peek()
"""
self.max_heap -1 -2
self.min_heap 3

sol = MedianFinder()
sol.add_num(1)
print(sol.get_median()) # 1
sol.add_num(3)
print(sol.get_median()) # 2
sol.add_num(2)
print(sol.get_median()) # 2

"""

"""
self.max_heap -1 -2
self.min_heap 3
sol = MedianFinder()
sol.add_num(1)
print(sol.get_median()) # 1
sol.add_num(3)
print(sol.get_median()) # 2
sol.add_num(2)
print(sol.get_median()) # 2
sol.add_num(0)
print(sol.get_median()) # 1.5


"""
"""
size max heap == 0
size min heap == 0
"""

sol = MedianFinder()
sol.add_num(3)
print(sol.get_median()) # 3
sol.add_num(2)
print(sol.get_median()) # 2.5
sol.add_num(1)
print(sol.get_median()) # 2
sol.add_num(0)
print(sol.get_median()) # 1.5