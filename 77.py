class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(i, path, k):
            if k == 0:
                res.append(path.copy())
                return
            if(i > n):
                return

            path.append(i)
            dfs(i + 1, path, k - 1)
            path.pop()
            dfs(i + 1, path, k)

        dfs(1, [], k)
        return res