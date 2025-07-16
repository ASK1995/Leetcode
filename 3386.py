class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longest_index, longest_time = None, 0
        prev = 0
        for index, time in events:
            diff = time - prev
            if(diff > longest_time):
                longest_time = time - prev
                longest_index = index
            elif(diff == longest_time):
                longest_index = min(index, longest_index)
            prev = time
        return longest_index