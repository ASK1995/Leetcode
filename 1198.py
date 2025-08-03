from collections import Counter

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        count = Counter()
        for row in mat:
            for val in row:
                count[val] += 1
                if(count[val] == len(mat)):
                    return val

        return -1