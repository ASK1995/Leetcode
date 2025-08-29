class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = set()

        def dfs(i, path, target):
            if(target == 0):
                res.add(tuple(path.copy()))
                return
            if(i == len(candidates) or target < 0):
                return
            path.append(candidates[i])
            dfs(i + 1, path, target - candidates[i])
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, path, target)

        dfs(0, [], target)
        return list(res)