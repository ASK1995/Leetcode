from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        c1, c2 = Counter(secret), Counter(guess)

        for n1, n2 in zip(secret, guess):
            if(n1 == n2):
                bulls += 1

        for key, value in c2.items():
            if(c1[key] != 0):
                cows += min(c1[key], value)

        return str(bulls) + "A" + str(cows - bulls) + "B"