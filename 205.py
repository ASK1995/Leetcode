from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = defaultdict(lambda:-1)
        mapped = set()

        for letter1, letter2 in zip(s, t):
            if(mapper[letter1] == -1):
                if(letter2 in mapped):
                    return False
                mapper[letter1] = letter2
            elif(mapper[letter1] != letter2):
                return False
            mapped.add(letter2)

        return True