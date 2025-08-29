class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        zeroes, ones = 0, 0
        left, right = 0, 0

        while(right < len(s)):
            if(s[right] == '1'):
                ones += 1
            else:
                zeroes += 1
            while(zeroes > k and ones > k):
                if(s[left] == '0'):
                    zeroes -= 1
                else:
                    ones -= 1
                left += 1
            res += right - left + 1
            right += 1
        
        return res