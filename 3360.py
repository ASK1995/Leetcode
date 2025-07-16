class Solution:
    def canAliceWin(self, n: int) -> bool:
            remove = 10
            alice = True
            while(remove <= n):
                n, remove = n - remove, remove - 1
                alice = not alice
            return True if not alice else False