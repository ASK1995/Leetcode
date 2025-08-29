class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for val in range(1, amount + 1):
            for coin in coins:
                if val - coin >= 0:
                    min_coins[val] = min(min_coins[val], 1 + min_coins[val - coin])
        
        return min_coins[amount] if min_coins[amount] != amount + 1 else -1