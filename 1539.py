class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        for i, num in enumerate(arr):
            if(num - prev - 1 < k):
                k -= (num - prev - 1)
            else:
                return prev + k
            prev = num

        return arr[-1] + k