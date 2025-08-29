class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        res, res_time = None, 0
        prev = 0

        for button, time in events:
            diff = time - prev
            if(diff > res_time):
                res_time = time - prev
                res = button
            elif(diff == res_time):
                res = min(button, res)
            prev = time

        return res