class Solution:
    def countAsterisks(self, s: str) -> int:
        inside = False
        num_stars = 0

        for letter in s:
            if(letter == '|'):
                inside = not inside
            elif(letter == '*' and not inside):
                num_stars += 1
        return num_stars