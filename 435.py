class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        start, end = intervals[0][0], intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            new_start, new_end = intervals[i][0], intervals[i][1]
            if(new_start < end):
                res += 1
            else:
                start, end = new_start, new_end
        return res