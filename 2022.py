class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if(m * n != len(original)):
            return []
        res = []
        i = 0
        for row in range(m):
            entry = []
            for column in range(n):
                entry.append(original[i])
                i += 1
            res.append(entry)
        return res