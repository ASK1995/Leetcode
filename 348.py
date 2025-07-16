class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = {1: [0 for i in range(n)], 2: [0 for i in range(n)]}
        self.columns = {1: [0 for i in range(n)], 2: [0 for i in range(n)]}
        
        self.left_diagonal = {1: 0, 2: 0}
        self.right_diagonal = {1: 0, 2: 0}

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[player][row] += 1
        self.columns[player][col] += 1

        if(row == col):
            self.left_diagonal[player] += 1
        if((row + col) == (self.n - 1)):
            self.right_diagonal[player] += 1

        if((self.rows[player][row] == self.n) or
        (self.columns[player][col] == self.n) or
        (self.left_diagonal[player] == self.n) or
        (self.right_diagonal[player] == self.n)):
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)