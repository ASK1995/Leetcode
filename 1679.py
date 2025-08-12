from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = 0

        for num in count.keys():
            if(k - num in count):
                if(k == 2 * num):
                    count[num] = count[num]//2
                res += min(count[k - num], count[num])
                count[k - num], count[num] = 0, 0

        return res