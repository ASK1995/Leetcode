from collections import defaultdict

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda:0)
        start = 0
        res = []
        for index, num in enumerate(nums):
            count[num] += 1
            if(index - start + 1 == k):
                res.append(len(count))
                count[nums[start]] -= 1
                if(count[nums[start]] == 0):
                    del count[nums[start]]
                start += 1
        return res