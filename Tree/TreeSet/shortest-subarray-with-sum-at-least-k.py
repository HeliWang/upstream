import sys


class MySolution:
    def binary_search(self, prefix_sum, prefix_stack, target):
        """
        find largest index on prefix_stack, the value on which is <= target
        if cannot find, return -1
        """
        i = 0
        j = len(prefix_stack)
        while i < j:
            mid = (i + j) // 2
            if target >= prefix_sum[prefix_stack[mid]]:
                i = mid + 1
            else:
                j = mid
        if i > 0 and prefix_sum[prefix_stack[i - 1]] <= target: return prefix_stack[i - 1]
        return -1

    def shortestSubarray(self, A, k):
        # substring -> think about prefix array
        # past prefix sum <= current prefix sum - k
        # we want to have a past prefix sum as close to current index as possible
        # first approach: O(n^2) -- iterate through all past prefix
        # second approach O(n*log(n)): want to have a left number < current num
        #   mono stack [min -> max]
        # then binary search for the max index with prefix sum <= current prefix sum - k
        n = len(A)
        prefix_sum = [0] * (n + 1)
        for i, num in enumerate(A):
            prefix_sum[i + 1] = prefix_sum[i] + num
        prefix_stack = []  # a stack of prefix_sum index, value on these indexes are sorted [min -> max]
        res_length = -1
        for i, prefix in enumerate(prefix_sum):
            while prefix_stack and prefix_sum[prefix_stack[-1]] > prefix:
                prefix_stack.pop()
            prefix_stack.append(i)
            last_prefix_index = self.binary_search(prefix_sum, prefix_stack, prefix - K)
            if last_prefix_index == -1: continue
            if res_length == -1 or res_length > (i - last_prefix_index):
                res_length = i - last_prefix_index
        return res_length


import Queue


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int

        所以要换个思路，对于每个以i结尾的子数组，有效的开头可能有很多；暴力的方法就是遍历每个有效的开头求最小的length，
        但是这些有效的开头都是有重叠的，
        一个优化的思路就是能不能每次不遍历所有有效开头，维护一个数据结构，每次都更新这个数据结构的value，从而避免重复运算

        https://www.gjxhlan.me/2018/07/07/leetcode-contest-91-solution/
        """
        # 如若有比K大的数，则直接返回1
        if max(A) >= K: return 1

        # 记录和，dp[i] = sum(A[:i])
        dp = [0] * (len(A) + 1)
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + A[i - 1]

        res = float('inf')
        # 初始化队列
        Q = Queue.deque([0])
        for i in range(1, len(dp)):
            # 思路中第2步
            while Q and dp[i] - dp[Q[0]] >= K:
                res = min(res, i - Q.popleft())
            # 思路中第3步
            while Q and dp[i] < dp[Q[-1]]:
                Q.pop()
            Q.append(i)
        return [res, -1][res == float('inf')]
