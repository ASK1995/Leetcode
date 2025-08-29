class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        i, j, k = 0, 0, 0
        while(i < len(arr1) and j < len(arr2) and k < len(arr3)):
            n1, n2, n3 = arr1[i], arr2[j], arr3[k]
            if(n1 == n2 and n1 == n3):
                res.append(n1)
                i, j, k = i + 1, j + 1, k + 1
            else:
                m = max(n1, n2, n3)
                if(n1 < m):
                    i += 1
                if(n2 < m):
                    j += 1
                if(n3 < m):
                    k += 1
        return res