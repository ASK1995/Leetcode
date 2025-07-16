class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bits = []
        goal_bits = []
        
        while(start != 0):
            start_bits.append(start % 2)
            start //= 2
        while(goal != 0):
            goal_bits.append(goal % 2)
            goal //= 2
        while(len(goal_bits) != len(start_bits)):
            if(len(goal_bits) < len(start_bits)):
                goal_bits.append(0)
            else:
                start_bits.append(0)
        res = 0
        for i in range(len(goal_bits)):
            if(goal_bits[i] != start_bits[i]):
                res += 1
        return res