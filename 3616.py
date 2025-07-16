class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        current_min, total = ranks[0], 0
        for rank in ranks:
            if(rank < current_min):
                total += 1
                current_min = rank
        return total