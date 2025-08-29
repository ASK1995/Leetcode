class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def dfs(i, last_zero, ans):
            if(i == n):
                res.append("".join(ans.copy()))
                return
            ans.append('1')
            dfs(i + 1, False, ans)
            ans.pop()
            if(not last_zero):
                ans.append('0')
                dfs(i + 1, True, ans)
                ans.pop()

        dfs(0, False, [])
        return res