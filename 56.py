class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        for index in range(1, len(intervals)):
            start, end = intervals[index][0], intervals[index][1]
            if(start <= prev_end):
                prev_end = max(end, prev_end)
            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = start, end
        res.append([prev_start, prev_end])
        return res