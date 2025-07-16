class Solution:
    def isHappy(self, n: int) -> bool:
        def compute(x):
            res = 0
            while(x != 0):
                res += (x %  10) ** 2
                x //= 10
            return res

        slow, fast = n, compute(n)
        while(slow != fast):
            slow = compute(slow)
            fast = compute(compute(fast))
        return slow == 1