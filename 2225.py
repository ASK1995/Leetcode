from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = defaultdict(lambda: [0, 0])

        for match in matches:
            win, loss = match[0], match[1]
            count[win][0] += 1
            count[loss][1] += 1

        ans0, ans1 = [], []
        keys = sorted(count)

        for key in keys:
            if(count[key][1] == 0):
                ans0.append(key)
            elif(count[key][1] == 1):
                ans1.append(key)

        return [ans0, ans1]