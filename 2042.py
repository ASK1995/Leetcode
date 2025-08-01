class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        text = s.split()
        prev = None

        for word in text:
            if(word.isdigit()):
                num = int(word)
                if(prev != None):
                    if(num <= prev):
                        return False
                prev = num

        return True