import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0

        heapq.heapify(nums)
        while(len(nums) != 0):
            x = heapq.heappop(nums)
            if(x >= k):
                heapq.heappush(nums, x)
                break
            res += 1
        
        return res