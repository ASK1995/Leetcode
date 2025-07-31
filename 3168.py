class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        max_chairs = 0
        for chair in s:
            if(chair == 'E'):
                chairs += 1
            elif(chair == 'L'):
                chairs -= 1
            max_chairs = max(max_chairs, chairs)
        return max_chairs