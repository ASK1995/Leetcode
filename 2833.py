class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r, d = 0, 0, 0

        for move in moves:
            if(move == 'L'):
                l += 1
            elif(move == 'R'):
                r += 1
            else:
                d += 1

        return abs(l - r) + d