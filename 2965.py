class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        miss, repeat = -1, -1
        nums = set()
        index, xor_total = 1, 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] in nums:
                    repeat = grid[row][col]
                nums.add(grid[row][col])
                xor_total ^= index ^ grid[row][col]
                index += 1

        return [repeat, xor_total ^ repeat]