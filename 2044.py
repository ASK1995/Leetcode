class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        max_or, current_or, count = 0, 0, 0

        def dfs(i, path):
            if(i == len(nums)):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)

        dfs(0, [])
        for values in res:
            current_or = 0
            for value in values:
                current_or = value | current_or
            if(current_or > max_or):
                max_or = current_or
                count = 1
            elif(current_or == max_or):
                count += 1

        return count