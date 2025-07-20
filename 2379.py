class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count('W')
        res = whites

        for index in range(k, len(blocks)):
            if blocks[index] == 'W':
                whites += 1
            if blocks[index - k] == 'W':
                whites -= 1
            res = min(res, whites)

        return res