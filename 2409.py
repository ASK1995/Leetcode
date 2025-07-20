class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        arrival = sum(days[:int(arrive[:2]) - 1]) + int(arrive[3:])
        departure = sum(days[:int(leave[:2]) - 1]) + int(leave[3:])

        res = max(departure - arrival + 1, 0)
        return res