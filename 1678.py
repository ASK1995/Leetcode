class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        index = 0
        while(index < len(command)):
            val = command[index]
            if(val == 'G'):
                res += 'G'
            elif(val == '('):
                if(command[index + 1] == ')'):
                    res += 'o'
                    index += 1
                else:
                    res += 'al'
                    index += 3
            index += 1
        return res