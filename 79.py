class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if(i == len(word)):
                return True
            if(r < 0 or c < 0 or r >= m or c >= n
            or word[i] != board[r][c] or (r, c) in visited):
                return False
            visited.add((r, c))
            res = False
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                res = res or dfs(r + x, c + y, i + 1)
            visited.discard((r, c))
            return res

        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0):
                    return True
        return False