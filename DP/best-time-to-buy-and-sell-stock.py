# III
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        # you must sell the stock before you buy again
        # You may complete at most two transactions.

        Not Buying Anything | Buy & Hold | Buy & Sell Already | Buy & Hold | Buy & Sell Already
        states[i][*]: some property including price[0]..price[i]
        states[i][0]: not buying anything = 0
        states[i][1]: first buy & holding (the current profit is price[i - 1] - price_buy)
        states[i][1] = max(states[i - 1][1] + prices[i - 1] - prices[i - 2], prices[i - 1] - prices[i - 2])
        states[i][2]: first buy & Sold already
        states[i][2] = max(states[i - 1][2], states[i][1])

        states[i][3]: second buy & holding (the current profit is price[i - 1] - price_buy)
        states[i][3] = max(states[i - 1][3] + prices[i - 1] - prices[i - 2], states[i][2])

        states[i][4]: second buy & Sold already
        states[i][4] = max(states[i - 1][4], states[i][3])

        Final Answer: max(states[n][0], states[n][2], states[n][4])
        Input: [3,3,5,0,0,3,1,4] Output: 6
               [1,2,3,4,5] Output: 4
               [1, 2, 1, 0] Output: 1

               [1, 2] Output: 1
               [1, -1] Output: 0
        """
        n = len(prices)
        states = [[0] * 5 for _ in range(n + 1)]
        for i, state in enumerate(states):
            if i <= 1: continue
            states[i][1] = max(states[i - 1][1] + prices[i - 1] - prices[i - 2], states[i][0])
            states[i][2] = max(states[i - 1][2], states[i][1])
            states[i][3] = max(states[i - 1][3] + prices[i - 1] - prices[i - 2], states[i][2])
            states[i][4] = max(states[i - 1][4], states[i][3])
        return states[n][4]

class Solution(object):
    def maxProfit(self, prices):
        """
        [5,8]
        [5,8,11]
        [5,8,3]
        [5,8,3,22]
        [5,8,3,22,145]
        [7,6,4,3,1]
        """
        n = len(prices)
        profit = [[0] * 2 for _ in range(n)]
        # profit[i][0]: max profit with up to one tranasaction finished on i-th day
        # profit[i][1]: max profit with up to two tranasactions finished on i-th day
        # profit[i][0] = max(profit[i - 1][0], prices[i] - prices[j])
        #    where prices[j] is the min price in prices[0..i]
        # profit[i][1] = max(profit[i - 1][1], prices[i] - prices[j] + profit[j][0])
        #              = max(profit[i - 1][1], prices[i] - (prices[j] - profit[j][0]))
        #    where prices[j] - profit[j][0] is the min value of the difference
        if not prices: return 0
        min_price = prices[0]
        min_diff  = prices[0] - profit[0][0]
        for i in range(1, n):
            profit[i][0] = max(profit[i - 1][0], prices[i] - min_price)
            profit[i][1] = max(profit[i - 1][1], prices[i] - min_diff)
            min_price    = min(min_price, prices[i])
            min_diff     = min(min_diff,  prices[i] - profit[i][0])
        return profit[n - 1][1]

class Solution(object):
    def maxProfit(self, prices):
        """
        [5,8]
        [5,8,11]
        [5,8,3]
        [5,8,3,22]
        [5,8,3,22,145]
        [7,6,4,3,1]
        """
        n = len(prices)
        profit_1t  = 0
        profit_2ts = 0
        # profit[i][0]: max profit with up to one tranasaction finished on i-th day
        # profit[i][1]: max profit with up to two tranasactions finished on i-th day
        # profit[i][0] = max(profit[i - 1][0], prices[i] - prices[j])
        #    where prices[j] is the min price in prices[0..i]
        # profit[i][1] = max(profit[i - 1][1], prices[i] - prices[j] + profit[j][0])
        #              = max(profit[i - 1][1], prices[i] - (prices[j] - profit[j][0]))
        #    where prices[j] - profit[j][0] is the min value of the difference
        if not prices: return 0
        min_price = prices[0]
        min_diff  = prices[0] - 0
        for i in range(1, n):
            profit_1t    = max(profit_1t,  prices[i] - min_price)
            profit_2ts   = max(profit_2ts, prices[i] - min_diff)
            min_price    = min(min_price, prices[i])
            min_diff     = min(min_diff,  prices[i] - profit_1t)
        return profit_2ts

# IV
# Classic Memory Limit Exceeded
class Solution(object):
    def maxProfit(self, k, prices):
        """
        Sol 1: Time O(n*k) Space O(k)
        profile[i][m] = max profile by trading until i-th day, by up to m transactions
        profile[i][m] = max(profile[i - 1][m], profile[i][m - 1], prices[i] - prices[j] + profile[j][m - 1])
                      = max(profile[i - 1][m], profile[i][m - 1], prices[i] - min_diff[m - 1])
                        where min_diff[m - 1] = min value of prices[j] - profile[j][m - 1] so far

        """
        n = len(prices)
        if not n: return 0
        profile = [[0] * (k + 1) for _ in range(n)]
        min_dff = [prices[0]] * (k + 1)
        for i in range(1, n):
            for m in range(1, k + 1):
                profile[i][m] = max(profile[i - 1][m], profile[i][m - 1], prices[i] - min_dff[m - 1])
                min_dff[m] = min(prices[i] - profile[i][m], min_dff[m])
            min_dff[0] = min(prices[i], min_dff[0])
        return profile[n - 1][k]

# what if k = 1000000000? very large
class Solution(object):
    def maxProfit(self, k, prices):
        """
        profile[i][m] = max profile by trading until i-th day, by up to m transactions
        profile[i][m] = max(profile[i - 1][m], profile[i][m - 1], prices[i] - prices[j] + profile[j][m - 1])
                      = max(profile[i - 1][m], profile[i][m - 1], prices[i] - min_diff[m - 1])
                        where min_diff[m - 1] = min value of prices[j] - profile[j][m - 1] so far
        There is a test case where k >>> len(prices) -- handle it as a special cases
        """
        n = len(prices)
        if not n: return 0
        if k >= n / 2:
            return self.quickSolve(n, prices)
        profile = [0] * (k + 1)
        min_dff = [prices[0]] * (k + 1)
        for i in range(1, n):
            for m in range(1, k + 1):
                profile[m] = max(profile[m], profile[m - 1], prices[i] - min_dff[m - 1])
                min_dff[m] = min(prices[i] - profile[m], min_dff[m])
            min_dff[0] = min(prices[i], min_dff[0])
        return profile[k]

    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution(object):
    def maxProfit(self, prices):
        """
        [1,2,3,0,2]

        profit[i][0] = holding the stock
          continue a trasaction and sell on day i: profit[i - 1][0] + prices[i] - prices[i - 1]
          start a new trasaction: profit[i - 1][1]
        profit[i][1] = cooldown on day i, max(profit[i - 1][1], profit[i - 1][0])
        return max(profit[n - 1])


        """
        n = len(prices)
        if not n: return 0
        profit = [[0] * 2 for _ in range(n)]
        for i in range(1, n):
            profit[i][0] = max(profit[i - 1][0] + prices[i] - prices[i - 1], profit[i - 1][1])
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0])
        return max(profit[n - 1])


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int

        value[i][0] = portfolio value when holding the stock on day i
            option1: new buy
              max(value[i - 1][0], value[i - 1][1]) - fee
            option2: continue a transaction as before
              value[i - 1][0] + prices[i] - prices[i - 1]

        value[i][1] = portfolio value when not holding the stock on day i
            option1: keep cooling down as one day before
              value[i - 1][1]
            option2: a new cool-down day
              value[i - 1][0]
        return max(value[n - 1])

        prices = [1, 3, 2, 8, 4, 9], fee = 2
        [
          [-2,  0],
          [0 ,  0],
          [-1,  0],
          [5 ,  0],
          [3 ,  5],
          [8 ,  5],
        ]
        """
        n = len(prices)
        value = [[0] * 2 for _ in range(n)]
        value[0][0] = 0 - fee
        value[0][1] = 0
        for i in range(1, n):
            value[i][1] = max(value[i - 1][0], value[i - 1][1])
            value[i][0] = max(value[i][1] - fee, value[i - 1][0] + prices[i] - prices[i - 1])
        return max(value[n - 1])
