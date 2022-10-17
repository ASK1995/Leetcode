class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        total = 0
        for index, pre in enumerate(pref):
            if(index == 0):
                total = total ^ pre
            else:
                total = pre ^ pref[index - 1]
            res.append(total)
        
        return res