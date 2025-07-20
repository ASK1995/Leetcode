class Solution:
    def isPalindrome(self, x: int) -> bool:
        num, rev = x, 0
        if(x < 0):
            return False
        while(x != 0):
            rev = rev * 10 + x % 10
            x //= 10
        return rev == num