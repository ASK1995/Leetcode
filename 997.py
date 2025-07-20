from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(lambda:[])
        trusts = defaultdict(lambda:[])
        for a, b in trust:
            trusted[b].append(a)
            trusts[a].append(b)
        judges = 0
        judge = -1
        for i in range(1, n + 1):
            if(len(trusts[i]) == 0):
                if(len(trusted[i]) == n - 1):
                    judges += 1
                    judge = i
        if(judges > 1 or judge == -1):
            return -1
        return judge