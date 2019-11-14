import functools


class SolutionMem:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequenceHelper(text1, len(text1) - 1, text2, len(text2) - 1)

    @functools.lru_cache
    def longestCommonSubsequenceHelper(self, text1: str, i, text2: str, j) -> int:
        if i < 0 or j < 0: return 0
        if text1[i] == text2[j]:
            return 1 + self.longestCommonSubsequenceHelper(text1, i - 1, text2, j - 1)
        else:
            return max(self.longestCommonSubsequenceHelper(text1, i - 1, text2, j),
                       self.longestCommonSubsequenceHelper(text1, i, text2, j - 1))


class SolutionDP:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        longest = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    longest[i][j] = 1 + longest[i - 1][j - 1]
                else:
                    longest[i][j] = max(longest[i - 1][j], longest[i][j - 1])
        return longest[n1][n2]
