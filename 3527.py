from collections import defaultdict

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(lambda:0)
        max_key, max_value = None, -1

        for response in responses:
            res = set()
            for word in response:
                res.add(word)
        
            for word in res:
                count[word] += 1
                if(count[word] > max_value):
                    max_key, max_value = word, count[word]
                elif(count[word] == max_value):
                    max_key = min(max_key, word)
        return max_key