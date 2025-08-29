from collections import defaultdict

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(lambda:0)
        max_key, max_value = None, -1

        for words in responses:
            words = set(words)

            for word in words:
                count[word] += 1
                if(count[word] > max_value):
                    max_key, max_value = word, count[word]
                elif(count[word] == max_value):
                    max_key = min(max_key, word)

        return max_key