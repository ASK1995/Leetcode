class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        res = ord(coordinate1[0]) + int(coordinate1[1])
        res += ord(coordinate2[0]) + int(coordinate2[1])

        return (res % 2 == 0)