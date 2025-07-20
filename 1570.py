from collections import defaultdict

class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_val = defaultdict(lambda:-1)
        for index, num in enumerate(nums):
            if(num != 0):
                self.index_val[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for key in self.index_val.keys():
            if(vec.index_val[key] != -1):
                res += self.index_val[key] * vec.index_val[key]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)