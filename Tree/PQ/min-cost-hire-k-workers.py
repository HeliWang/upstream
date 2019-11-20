from heapq import heappush, heappop


class MaxHeapLowestK():  # size k, max heap, store lowest k qualities so far
    def __init__(self, k):  # K > 0
        self.k = k
        self.heap = []
        self.sum_heap = 0

    def max_heap_peek(self):
        if self.heap: return 0 - self.heap[0]

    def max_heap_pop(self):
        if self.heap:
            pop = 0 - heappop(self.heap)
            self.sum_heap -= pop
            return pop

    def max_heap_push(self, x):
        if self.k == len(self.heap):  # Compare with head whenever the heap
            # is full
            if x <= self.max_heap_peek():  # lower than head, pop
                self.max_heap_pop()
            else:  # abandob
                return
        heappush(self.heap, 0 - x)  # two possibility: not full -> direct add.
        # Full -> pop and add
        self.sum_heap += x


class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float

        Input: quality = [10,20,5], wage = [70,50,30], K = 2
        Output: 105.00000
        Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

        # Time Complexity O(n*logn)
        # Space Complexity O(n)
        """
        rate_wage_quality = map(lambda x: (x[0] / x[1], x[0], x[1]), zip(wage, quality))
        rate_wage_quality = sorted(rate_wage_quality)
        heap = MaxHeapLowestK(K)
        result = sys.maxsize
        for i, v in enumerate(rate_wage_quality):
            rate, wage, quality = v
            heap.max_heap_push(quality)
            if i >= K - 1:
                result = min(result, heap.sum_heap * rate)
        return result
