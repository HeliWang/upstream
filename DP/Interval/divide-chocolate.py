class SolutionRecursion(object):
    def maximizeSweetnessHelper(self, sweetness, K, i):
        if K == 0:
            return sum(sweetness[:i + 1])
        res = - sys.maxsize
        for j in range(i):
            rec_res = self.maximizeSweetnessHelper(sweetness, K - 1, j)
            cur_val = sum(sweetness[j + 1:i + 1])
            res = max(res, min(cur_val, rec_res))
        return res

    def maximizeSweetness(self, sweetness, K):
        return self.maximizeSweetnessHelper(sweetness, K, len(sweetness) - 1)


class SolutionMem(object):
    def maximizeSweetnessHelper(self, sweetness, K, i):
        if K == 0:
            return sum(sweetness[:i + 1])
        if (K, i) in self.cache:
            return self.cache[(K, i)]
        res = - sys.maxsize
        for j in range(i):
            rec_res = self.maximizeSweetnessHelper(sweetness, K - 1, j)
            cur_val = sum(sweetness[j + 1:i + 1])
            res = max(res, min(cur_val, rec_res))
        self.cache[(K, i)] = res
        return res

    def maximizeSweetness(self, sweetness, K):
        self.cache = {}
        return self.maximizeSweetnessHelper(sweetness, K, len(sweetness) - 1)


class SolutionDP(object):
    def maximizeSweetness(self, sweetness, K):
        """
        DP O(n^2*k)
        """
        n = len(sweetness)
        if not n: return 0
        self.max_sweet = [None] * n
        self.max_sweet[0] = sweetness[0]
        for i in range(1, n):
            self.max_sweet[i] = self.max_sweet[i - 1] + sweetness[i]
        self.max_sweet_new = [None] * n
        for k in range(K):
            for i in range(n):
                res = - sys.maxsize
                for j in range(i):
                    cur_val = sum(sweetness[j + 1:i + 1])  # we can use prefix-sum to reduce time
                    res = max(res, min(cur_val, self.max_sweet[j]))
                self.max_sweet_new[i] = res
            self.max_sweet, self.max_sweet_new = self.max_sweet_new, self.max_sweet
        return self.max_sweet[-1]


class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        # Binary Search O(log(10^9) * n)
        n = len(sweetness)
        if not n: return 0
        if K == 0: return sum(sweetness)
        l = min(sweetness)
        r = sum(sweetness)
        while l < r:
            mid = (l + r) // 2
            count = 0
            sweet_so_far = 0
            for i, sweet in enumerate(sweetness):
                sweet_so_far += sweet
                if sweet_so_far >= mid:
                    count += 1
                    sweet_so_far = 0
            if count < K + 1:
                r = mid
            else:
                l = mid + 1
        return l - 1
