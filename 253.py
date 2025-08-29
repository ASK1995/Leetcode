class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        res, count = 0, 0
        i, j = 0, 0
        while(i < len(starts) and j < len(ends)):
            if(starts[i] < ends[j]):
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)
        return res