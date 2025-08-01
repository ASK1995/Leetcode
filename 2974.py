import heapq

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        arr = []

        while(len(nums) != 0):
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            arr.append(b)
            arr.append(a)
        
        return arr