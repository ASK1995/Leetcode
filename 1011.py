class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while(l <= r):
            m = (l + r)//2
            current = 0
            count = 1
            for weight in weights:
                if(weight + current <= m):
                    current += weight
                else:
                    current = weight
                    count += 1
            if(count <= days):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res