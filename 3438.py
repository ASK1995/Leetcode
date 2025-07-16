from itertools import pairwise

class Solution:
    def findValidPair(self, s: str) -> str:
        count = [0]*10
        for letter in s:
            digit = int(letter)
            count[digit] += 1
        for num1, num2 in pairwise(map(int, s)):
            if(num1 != num2 and count[num1] == num1 and count[num2] == num2):
                return str(num1) + str(num2) 
        return ""