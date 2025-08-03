class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res = 0
        i = len(cost) - 1

        while(i - 2 >= 0):
            res += cost[i] + cost[i - 1]
            i -= 3
        
        while(i >= 0):
            res += cost[i]
            i -= 1

        return res