class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(i, j, index):
            if(index == len(word)):
                return True
            if(i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[index] or (i, j) in visited):
                return False
            visited.add((i, j))
            res = False
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                res = res or dfs(i + x, j + y, index + 1)
            visited.discard((i, j))
            return res

        for i in range(m):
            for j in range(n):
                if(dfs(i, j, 0)):
                    return True
        return False
        