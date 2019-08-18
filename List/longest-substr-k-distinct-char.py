import collections

"""
(1) Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        lo, ans, d = 0, 0, collections.defaultdict(int)
        for hi in range(len(s)):
            d[s[hi]] += 1
            # substr is s[lo:hi + 1]
            while len(d) == k + 1:
                d[s[lo]] -= 1
                if d[s[lo]] == 0: del d[s[lo]]
                lo += 1
            ans = max(ans, hi + 1 - lo)

        return ans


"""
(2) What if the input is a stream of data? Limited time complexity to O(n * log n)
"""


class LongestSubstr(object):
    def __init__(self, k):
        self.k = k
        self.ans = 0
        self.counter = 0  # how many chars has passed by
        self.char_index = collections.defaultdict()
        self.last_occurance = IndexMinPQ()


def accept(self, c):
    """Accept a char from the data stream
    if char in cache:

    if char not in cache:
      if self.dist_char == self.k:
        remove prefix until a dist char disappear from the current substr
        reduce self.cur_substr_len accordingly
    """
    if c not in self.char_index:
        count_dist_nums = self.inc - self.last_occurance.min()[0]
        if count_dist_nums == self.k:
            _, old_c = self.last_occurance.delete_min()
            del self.char_index[old_c]
        i = self.last_occurance.insert(self.inc, c)
        self.char_index[c] = i
    else:

    # find the index of
    self.char_last_occurance[c]
    self.inc += 1


def longest_substr_len(self):
    """
    return: the length of longest string so far
    """


class IndexMinPQ(object):
    """
    Assume insert(key, priority), update_priority(key, new_priority), delete(key), delete_min() operations are all in O(log n) time complexity
    The contains(key), find(key) -> priority, get_min operations are in O(1)

    Implementation:
    # map: key (char) -> (priority, index in the pq array)
    # self.pq is an array of keys (chars), compared by the key (char)'s priority by looking up the map
    """
    def __init__(self):
        pass

    def insert(self, char, priority):
        pass

    def contains(self, char):
        pass

    def find(self, char):
        pass

    def remove(self, char):
        pass

    def update(self, char, new_priority):
        pass

    def min(self):
        pass

    def delete_min(self):
        pass

    def size(self):
        pass


"""
(3) What if the input is a stream of data? Limited time complexity to O(n)
"""
class LongestSubstr(object):
    def __init__(self):
        pass

    def accept(self, char):
        """Accept a char from the data stream
        """

    def longest_substr(self):
        """
        return: the length of longest string so far
        """


# 下面这个对1的solution是我自己写的，又丑又长
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        i = 0  # start index of the substr
        j = 0  # end index of the substr
        char_count = collections.Counter()
        total_dist_char = 0
        res = 0
        while j < len(s):
            # move j forward so that s[i:j] will contains at most k dist char
            while j < len(s) and total_dist_char <= k:  # (1)
                char = s[j]  ####### should be s[j]!!!!!!
                if char_count[char] == 0 and total_dist_char == k: break
                if char_count[char] == 0:
                    total_dist_char += 1
                char_count[char] += 1
                j += 1
            res = max(res, j - i)
            # move i forward to remove one dist char
            while i < len(s) and total_dist_char == k:  # (2)
                char = s[i]
                char_count[char] -= 1
                if char_count[char] == 0:
                    total_dist_char -= 1
                i += 1
        return res
    #  Spend 20 mins to finish


"""
Test:
 s = "eceba" k = 2
 i = 0, j = 0
 res = max([3, ])
 after (1): 
   total_dist_char = 2, j = 3
   char_count = {e: 2, c : 1}
 after (2): i = 2
   char_count = {e: 1, c : 0}
   total_dist_char = 1

 after (1): 
   total_dist_char = 2, j = 4
   char_count = {e: 1, c : 0, b:1}
 after (2): i = 3
   char_count = {e: 0, c : 0, b:1}}

 after (1): 
   total_dist_char = 2, j = 5
   char_count = {e: 1, c : 0, b:1, a:1}
 after (2): i = 4
   char_count = {e: 0, c : 0, b:0, a:1}}
"""
