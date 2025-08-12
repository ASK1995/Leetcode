class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res, count = 0, 0
        left = 0

        for index, letter in enumerate(s):
            if(letter in vowels):
                count += 1
            if(index - left + 1 == k):
                res = max(res, count)
                if(s[left] in vowels):
                    count -= 1
                left += 1

        return res