class Solution:
    def confusingNumber(self, N):
        stN = str(N)
        if len(stN) == 1:
            return N in ["6", "9"]
        for i in range(len(stN)):
            if stN[i] not in ["6", "8", "9", "0", "1"]:
                return False
        for i in range(len(stN) // 2):
            j = len(stN) - 1 - i
            if (stN[i], stN[j]) not in [("8", "8"), ("0", "0"), ("6", "9"), ("9", "6"), ("1", "1")]:
                return True
        if len(stN) % 2 == 1 and stN[len(stN) // 2] not in "018":
            return True
        return False

    def confusingNumberCount(self, size):
        # subtracting the number of strobogrammatic numbers from the total
        if size == 0:
            return 0
        if size == 1:
            return 2  # 6, 9
        # 0 1 6 8 9
        total = 4 * (5 ** (size - 1))
        strobogrammatic = 4  # (1, 1), (8, 8), (6, 9), (9, 6)
        strobogrammatic *= (5 ** ((size - 2) // 2))  # (0, 0), (1, 1), (8, 8), (6, 9), (9, 6)
        if size % 2 == 1:
            strobogrammatic *= 3  # middle 0/1/8
        return total - strobogrammatic

    def dfs(self, cur_num, N):
        if cur_num <= N:
            if self.confusingNumber(cur_num):
                self.count += 1
            for i in [0, 1, 6, 8, 9]:
                if cur_num == 0 and i == 0: continue
                self.dfs(cur_num * 10 + i, N)

    def confusingNumberII(self, N):
        if N < 6: return 0
        if N < 9: return 1
        if N < 10: return 2
        self.count = 2
        self.dfs(0, N)
        return self.count
