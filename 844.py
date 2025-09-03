class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next(word, index):
            backspaces = 0
            while(index >= 0):
                if word[index] == '#':
                    backspaces += 1
                elif backspaces == 0 and index != '#':
                    break
                else:
                    backspaces -= 1
                index -= 1

            return index

        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = get_next(s, i)
            j = get_next(t, j)

            letter1 = s[i] if i >= 0 else "" 
            letter2 = t[j] if j >= 0 else ""

            if(letter1 != letter2):
                return False
            i, j = i - 1, j - 1
        return True