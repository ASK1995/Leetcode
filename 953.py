from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = defaultdict(lambda:-1)
        for i, letter in enumerate(order):
            index[letter] = i
        for i in range(20):
            prev = -1
            correct = True
            for word in words:
                current = -1 if i >= len(word) else index[word[i]]
                if(current < prev):
                    return False
                elif(current == prev):
                    correct = False
                prev = current
            if correct:
                return True
        return True