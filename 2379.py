class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        res = len(blocks)
        left = 0

        for index in range(k):
            if blocks[index] == 'W':
                whites += 1

        res = min(res, whites)
        for index in range(k, len(blocks)):
            if blocks[index] == 'W':
                whites += 1
            if blocks[left] == 'W':
                whites -= 1
            left += 1
            res = min(res, whites)

        return res