class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        current, longest = 0, 0
        res = 0
        for employee, time in logs:
            current = time - current
            if(current > longest):
                res = employee
                longest = current
            elif(current == longest):
                res = min(res, employee)
            current = time
        return res