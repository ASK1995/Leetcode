class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = 0
        for index in range(len(colors)):
            c1 = colors[index - 1]
            c2 = colors[index]
            if(index + 1 >= len(colors)):
                index = -1
            c3 = colors[index + 1]

            if(c2 != c1 and c2 != c3):
                res += 1
        return res