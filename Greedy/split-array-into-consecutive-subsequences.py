"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/

O(n*logk) using PQ
https://www.lizenghai.com/archives/20423.html
"""
import collections


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dic_heap = collections.defaultdict(list)  # 每个key的默认值是一个空列表
        for num in nums:
            if len(dic_heap[num - 1]) == 0:  # 没有以num-1为结尾的key
                heapq.heappush(dic_heap[num], 1)  # 以num为结尾的初始长度为1
            else:  # 弹出以num-1为结尾的key, 将以num为结尾的key压入, 并更新长度
                lens = heapq.heappop(dic_heap[num - 1])
                heapq.heappush(dic_heap[num], lens + 1)
        for key in dic_heap.keys():
            for lens in dic_heap[key]:
                if lens < 3:  # 如果列表中有小于3的长度
                    return False
        return True


"""Greedy, time O(n), space O(n)
https://www.jianshu.com/p/b910737af4dc

先遍历数组得到每个num出现的frequency。
对于每个num来说，要么将它append到已经成型的sequence中，要么以它为起点开辟一个新的长度为3的sequence。如果两者皆不可行，则返回false。
"""


def isPossible(self, nums):
    left = collections.Counter(nums)
    end = collections.Counter()
    for i in nums:
        if not left[i]: continue
        left[i] -= 1
        if end[i - 1] > 0:
            end[i - 1] -= 1
            end[i] += 1
        elif left[i + 1] and left[i + 2]:
            left[i + 1] -= 1
            left[i + 2] -= 1
            end[i + 2] += 1
        else:
            return False
    return True
