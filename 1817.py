from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        count = defaultdict(lambda : set())
        res = [0] * k
        for log in logs:
            user, time = log[0], log[1]
            count[user].add(time)
        for key, value in count.items():
            res[len(value) - 1] += 1
        return res