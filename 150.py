class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []

        for token in tokens:
            if(token == '+'):
                n2 = l.pop()
                n1 = l.pop()
                l.append(n1 + n2)
            elif(token == '-'):
                n2 = l.pop()
                n1 = l.pop()
                l.append(n1 - n2)
            elif(token == '*'):
                n2 = l.pop()
                n1 = l.pop()
                l.append(n1 * n2)
            elif(token == '/'):
                n2 = l.pop()
                n1 = l.pop()
                l.append(int(n1/n2))
            else:
                l.append(int(token))

        return l[0]