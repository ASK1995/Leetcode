class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0

        for operation in operations:
            x, y = operation[0], operation[-1]
            if(x == "+" or y == "+"):
                res += 1
            elif(x == "-" or y == "-"):
                res -= 1
        
        return res