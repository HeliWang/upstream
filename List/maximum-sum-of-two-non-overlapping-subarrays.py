class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # build accumulated sum with length L
        accu_L = []
        current_L = sum(A[:L])
        accu_L.append(current_L)
        for i in range(L, len(A)):
            current_L = current_L + A[i] - A[i - L]
            accu_L.append(current_L)

        # left_max array of max's accu_L
        left_max = []
        x = accu_L[0]
        for i in accu_L:
            x = max(x, i)
            left_max.append(x)

        # right_max array of max's accu_L
        right_max = []
        x = accu_L[-1]
        for i in accu_L[::-1]:
            x = max(x, i)
            right_max.append(x)
        right_max = right_max[::-1]
        res = 0

        current_M = sum(A[:M])
        for i in range(M - 1, len(A)):
            if i != M - 1:
                current_M = current_M + A[i] - A[i - M]
            current_max = current_M
            if i - M - L + 1 >= 0:
                current_max = max(current_max, left_max[i - M - L + 1] + current_M)
            if i < len(right_max) - 1:
                current_max = max(current_max, right_max[i + 1] + current_M)
            res = max(res, current_max)
        return res
