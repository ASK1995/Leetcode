class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        i = 0
        p = p.split('*')

        for letter in p:
            index = s.find(letter, i)
            if(index == -1):
                return False
            i = index + len(letter)

        return True