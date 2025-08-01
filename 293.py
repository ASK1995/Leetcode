class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        for i, val in enumerate(currentState):
            if(i == len(currentState) - 1):
                continue
            if(currentState[i] == '+' and currentState[i + 1] == '+'):
                entry = currentState[:i] + '--' + currentState[i + 2:]
                res.append(entry)
        return res