class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, target):
            if(target == 0):
                res.append(path.copy())
                return
            if(i == len(candidates) or target < 0):
                return
            path.append(candidates[i])
            dfs(i, path, target - candidates[i])
            path.pop()
            dfs(i + 1, path, target)

        dfs(0, [], target)
        return res