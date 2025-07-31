class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        i = 0

        while(i < len(s)//2):
            if(s[i].lower() in vowels):
                count += 1
            i += 1
        
        while(i < len(s)):
            if(s[i].lower() in vowels):
                count -= 1
            i += 1

        return count == 0