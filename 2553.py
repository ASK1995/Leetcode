class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            x = str(num)
            for letter in x:
                res.append(int(letter))

        return res