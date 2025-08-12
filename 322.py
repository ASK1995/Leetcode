class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [amount + 1] * (amount + 1)
        res[0] = 0

        for value in range(amount + 1):
            for coin in coins:
                if value - coin >= 0:
                    res[value] = min(res[value], 1 + res[value - coin])

        return res[amount] if res[amount] != amount + 1 else -1