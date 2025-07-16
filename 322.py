class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float('inf')] * (amount + 1)
        res[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i], 1 + res[i - coin])
        return res[amount] if res[amount] != float('inf') else -1