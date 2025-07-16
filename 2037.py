class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0

        for index in range(len(seats)):
            res += abs(seats[index] - students[index])
        return res