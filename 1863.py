class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        total_xor, current_xor = 0, 0

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
            current_xor = 0
            for value in values:
                current_xor ^= value
            total_xor += current_xor
        return total_xor