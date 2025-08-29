from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(not digits):
            return []
        mapper = defaultdict(lambda:"")
        
        mapper['2'] = "abc"
        mapper['3'] = "def"
        mapper['4'] = "ghi"
        mapper['5'] = "jkl"
        mapper['6'] = "mno"
        mapper['7'] = "pqrs"
        mapper['8'] = "tuv"
        mapper['9'] = "wxyz"
        res = []

        def dfs(i, path):
            if(i == len(digits)):
                res.append("".join(path.copy()))
                return
            for val in mapper[digits[i]]:
                path.append(val)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res