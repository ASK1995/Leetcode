class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(i, path, opens):
            if(i == n*2):
                if(opens == 0):
                    res.append("".join(path.copy()))
                return
            if(opens > 0):
                path.append(')')
                dfs(i + 1, path, opens - 1)
                path.pop()
            path.append('(')
            dfs(i + 1, path, opens + 1)
            path.pop()

        dfs(0, [], 0)
        return res