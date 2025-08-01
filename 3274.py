class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        res = ord(coordinate1[0]) + ord(coordinate1[1])
        res += ord(coordinate2[0]) + ord(coordinate2[1])

        return (res % 2 == 0)