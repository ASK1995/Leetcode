from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = defaultdict(lambda:-1)

        for index, num in enumerate(nums):
            if(last[num] != -1):
                if(index - last[num] <= k):
                    return True
            last[num] = index

        return False