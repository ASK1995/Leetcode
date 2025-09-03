class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        ans = ""

        def dfs(path, n):
            nonlocal ans
            if ans != "":
                return
            if(n == 0):
                val = "".join(path.copy())
                if(val not in nums):
                    ans = val
                return
            path.append('0')
            dfs(path, n - 1)
            path.pop()
            path.append('1')
            dfs(path, n - 1)
            path.pop()

        dfs([], n)
        return ans