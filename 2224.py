class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hour, minute = current.split(":")
        total1 = int(hour)*60 + int(minute)
        
        hour, minute = correct.split(":")
        total2 = int(hour)*60 + int(minute)
        
        total = total2 - total1
        count = 0
        times = [1, 5, 15, 60]
        times = times[::-1]
        for time in times:
            if(total - time >= 0):
                count += total//time
                total %= time

        return count