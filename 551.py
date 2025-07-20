class Solution:
    def checkRecord(self, s: str) -> bool:
        a, l = 0, 0
        late_count = False

        for i in s:
            if(i == 'A'):
                a += 1
            if(i == 'L'):
                if(not late_count):
                    late_count = True
                    l = 1
                else:
                    l += 1
            else:
                late_count = False
                if(l >= 3):
                    return False
        if(l >= 3 or a >= 2):
            return False
        return True