class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = None
        max_time, prev = 0, 0

        for index in range(len(releaseTimes)):
            time = releaseTimes[index] - prev
            if(time > max_time):
                max_time = time
                res = keysPressed[index]
            elif(time == max_time):
                res = max(res, keysPressed[index])
            prev = releaseTimes[index]
        return res