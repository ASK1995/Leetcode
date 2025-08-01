class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = set(["a", "e", "i", "o", "u"])
        res = ""
        
        for index, word in enumerate(words):
            if(word[0].lower() in vowels):
                res += word + "ma"
            else:
                res += word[1:] + word[0] + "ma"
            
            res += "a"*(index+1)
            res += " "
        
        return res[:-1]