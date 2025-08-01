class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if(numOnes >= k):
            return k
        elif(numZeros + numOnes >= k):
            return numOnes
        else:
            k -= numZeros + numOnes
            return numOnes - k
        return -1