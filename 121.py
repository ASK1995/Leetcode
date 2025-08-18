class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_cost = prices[0]

        for price in prices:
            min_cost = min(min_cost, price)
            max_profit = max(max_profit, price - min_cost)

        return max_profit