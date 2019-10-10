class Solution(object):
    def integerBreak(self, n):
        """
        integerBreak(i) is increasing as i increases

        integerBreak(n)
          max of
            1 * integerBreak(n - 1)
            2 * integerBreak(n - 2)
            3 * integerBreak(n - 3)
            ...
            (n - 1) * integerBreak(1)

        integerBreak(n + 1)
          max of
            1 * integerBreak(n + 1 - 1)
            2 * integerBreak(n + 1 - 2) = 2 * integerBreak(n - 1) = integerBreak(n - 1) + integerBreak(n - 1)
            3 * integerBreak(n + 1 - 3) = 3 * integerBreak(n - 2) = 2 * integerBreak(n - 2) + integerBreak(n - 2)

        Optimize to O(n) time by observing that the
          integerBreak(n) = max(...) = (n - y) * integerBreak(y)
          integerBreak(n + 1) = max(...) = (n + 1 - z) * integerBreak(z)
          z must be greater than y
        """
        max_prod = [1] * (n + 1)
        j = 1  # the last integer that leads to the result of max_prod[i]
        for i in range(2, n + 1):
            max_prod[i] = max_prod[i - 1]
            for k in range(j, i):
                if (i - k) * max(max_prod[k], k) >= max_prod[i]:
                    max_prod[i] = (i - k) * max(max_prod[k], k)
                    j = k
                else:
                    break
        return max_prod[n]
