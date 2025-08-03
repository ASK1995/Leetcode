class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k = k %  (2*n - 2)

        if(k < n):
            return k
        else:
            k -= n - 1

        return n - 1 - k