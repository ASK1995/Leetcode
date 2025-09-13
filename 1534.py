class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        count = [0]*1001

        for j in range(len(arr) - 1):
            for k in range(j + 1 , len(arr)):
                if(abs(arr[j] - arr[k]) <= b):
                    l = max(arr[j] - a, arr[k] - c)
                    r = min(arr[j] + a, arr[k] + c)
                    l = max(0, l)
                    r = min(r, 1000)
                    if l <= r:
                        res += count[r] - (count[l - 1] if l > 0 else 0)
            for i in range(arr[j], 1001):
                count[i] += 1

        return res