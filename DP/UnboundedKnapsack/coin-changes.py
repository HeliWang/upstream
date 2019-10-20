# Recursion
class Solution(object):
    def coinChangeRec(self, coins, amount, n):
        """
        What is the definition of the recursion:
        Returns min money by coins[:n] or -1
        """
        # What is the base case
        if amount == 0:
            return 0
        if n == 0:
            return -1
        #  Find the sub-problem:

        # collection of coins not including coins[n - 1]
        res = self.coinChangeRec(coins, amount, n - 1)

        # collection of coins including coins[n - 1]
        if amount >= coins[n - 1]:
            res_selected = self.coinChangeRec(coins, amount - coins[n - 1], n)
            # res_selected can be -1 or >= 0
            # if res_selected != -1, then the # of coins used will be res_selected + 1
            # 这个地方太容易错了！
            if res != -1 and res_selected != -1:
                res = min(res, res_selected + 1)
            elif res == -1 and res_selected != -1:
                res = res_selected + 1
            # if res != -1 but res_selected == -1
            # if res == -1 but res_selected == -1
        return res

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.coinChangeRec(coins, amount, len(coins))
