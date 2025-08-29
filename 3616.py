class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        replacements = 0
        current = ranks[0]

        for rank in ranks:
            if(rank < current):
                current = rank
                replacements += 1

        return replacements