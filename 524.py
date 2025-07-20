class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        def check(word1, word2):
            l1, l2 = 0, 0
            while(l1 < len(word1) and l2 < len(word2)):
                if(word1[l1] == word2[l2]):
                    l1, l2 = l1 + 1, l2 + 1
                else:
                    l2 += 1
            if(l1 == len(word1)):
                return True
            return False 

        for word in dictionary:
            exists = check(word, s)
            if(exists):
                if(len(word) > len(res)):
                    res = word
                elif(len(word) == len(res)):
                    res = min(res, word)
        return res