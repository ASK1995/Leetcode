class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        res = arrivalTime + delayedTime

        if(res >= 24):
            res -= 24

        return res