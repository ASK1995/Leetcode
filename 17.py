from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(not digits):
            return []
        mapper = defaultdict(lambda:"")
        
        mapper[2] = "abc"
        mapper[3] = "def"
        mapper[4] = "ghi"
        mapper[5] = "jkl"
        mapper[6] = "mno"
        mapper[7] = "pqrs"
        mapper[8] = "tuv"
        mapper[9] = "wxyz"
        
        res = ['']

        for letter in digits:
            digit = mapper[int(letter)]
            res = [letter1 + letter2 for letter1 in res for letter2 in digit]
        return res