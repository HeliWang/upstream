"""
837. New 21 Game
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points. 
 During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  
 Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:
Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.

Example 2:
Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.732

Note:
0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.

class Solution(object):
    def new21Game(self, N, K, W):
"""


# < O(W^K)
class Solution(object):
    def dfs(self, point, prob):
        if point >= self.K:
            self.prob_map[point] += prob
            return
        for i in range(1, self.W + 1):
            self.dfs(point + i, prob / self.W)

    def new21Game(self, N, K, W):
        self.N, self.K, self.W = N, K, W
        self.prob_map = [0] * (K + W)  # from 0 to K - 1 + W
        self.dfs(0, 1)
        return sum(self.prob_map[:N + 1])


# O(N * K)
class Solution(object):
    def new21Game(self, N, K, W):
        self.prob_map = [0] * (K + W)  # from 0 to K - 1 + W
        self.prob_map[0] = 1
        for i in range(0, K):
            for j in range(1, W + 1):
                self.prob_map[i + j] += self.prob_map[i] / W
        return sum(self.prob_map[K:N + 1])


# pr[i] = probability of reaching i
# pr[0] = 1
# ps[i] = pr[0] + pr[1] + ... + pr[i]
# then pr[i] = (pr[i - 1] + .... + pr[i - W]) / W = (ps[i - 1] - ps[i - W - 1]) / W
# But please be careful when i >= K since pr[i] = (pr[min(K, i - 1] + .... + pr[i - W]) / W  if i >= k
# O(N)
class Solution(object):
    def new21Game(self, N, K, W):
        if K == 0:
            return 1
        self.ps = [0] * (K + W)  # from 0 to K - 1 + W
        self.ps[0] = 1
        for i in range(1, K + W):
            if i >= W + 1:
                self.ps[i] = self.ps[i - 1] + (self.ps[min(K - 1, i - 1)] - self.ps[i - W - 1]) / W
            else:
                self.ps[i] = self.ps[i - 1] + self.ps[min(K - 1, i - 1)] / W
        return float(self.ps[N] - self.ps[K - 1])
