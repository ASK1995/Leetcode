class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(i, path, k, prev):
            if(i == len(nums)):
                if(k <= 0):
                    res.add(tuple(path.copy()))
                return
            if(nums[i] >= prev):
                path.append(nums[i])
                dfs(i + 1, path, k - 1, nums[i])
                path.pop()
            dfs(i + 1, path, k, prev)

        dfs(0, [], 2, float('-inf'))
        return list(res)