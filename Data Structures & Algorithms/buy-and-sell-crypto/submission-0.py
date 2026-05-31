class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i+1
        profit = 0

        while j < len(prices):
            curr_profit = 0
            if prices[i] > prices[j]:
                i = j
                j += 1
            else:
                curr_profit = prices[j] - prices[i]
                profit = max(profit, curr_profit)
                j += 1

        return profit


        