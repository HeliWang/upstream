# Good Way
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtracking(start, target, cur):
            if target == 0:
                res.append(cur[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                backtracking(i + 1, target - candidates[i], cur)
                cur.pop(-1)

        # for i in range(len(candidates)):
        backtracking(0, target, [])

        return res


# Traverse Way
class Solution(object):
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        results = []

        def comb(i, res, res_sum):
            if res_sum == target:
                results.append(list(res))
                return
            if res_sum > target or i >= len(candidates):
                return
            num = candidates[i]
            j = i
            while j < len(candidates) and candidates[j] == num:
                j += 1
            num_times = j - i
            comb(j, res, res_sum)  # zero num appears in the combination
            for time in range(1, num_times + 1):
                comb(j, res + [num] * time, res_sum + num * time)

        comb(0, [], 0)
        return results


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ways = [0] * (target + 1)
        ways[0] = 1
        for t in range(target + 1):
            for num in nums:
                if num <= t:
                    ways[t] += ways[t - num]
        return ways[target]
