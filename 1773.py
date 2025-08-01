class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        for item in items:
            val, color, name = item[0], item[1], item[2]
            if(ruleKey == "color"):
                if(ruleValue == color):
                    count += 1
            elif(ruleKey == "name"):
                if(ruleValue == name):
                    count += 1
            elif(ruleKey == "type"):
                if(ruleValue == val):
                    count += 1

        return count