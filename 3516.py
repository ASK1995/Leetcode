class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p1, p2 = abs(z - x), abs(z - y)
        if(p1 > p2):
            return 2
        elif(p2 > p1):
            return 1
        else:
            return 0