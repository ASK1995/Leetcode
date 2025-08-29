class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_start, new_end = newInterval[0], newInterval[1]
        for index, interval in enumerate(intervals):
            start, end = interval[0], interval[1]
            if(new_end < start):
                res.append([new_start, new_end])
                return res + intervals[index:]
            elif new_start > end:
                res.append(interval)
            else:
                new_start, new_end = min(start, new_start), max(end, new_end)

        res.append([new_start, new_end])
        return res