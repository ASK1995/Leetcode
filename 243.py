class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d1, d2 = None, None
        shortest = float('inf')
        for index, word in enumerate(wordsDict):
            if(word == word1):
                d1 = index
            elif(word == word2):
                d2 = index

            if(d1 != None and d2 != None):
                shortest = min(shortest, abs(d1 - d2))
        return shortest