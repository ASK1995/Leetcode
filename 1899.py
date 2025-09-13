class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        cur_a, cur_b, cur_c = 0, 0, 0

        for x, y, z in triplets:
            a1, b1, c1 = max(cur_a, x), max(cur_b, y), max(cur_c, z)
            if(a1 <= a and b1 <= b and c1 <= c):
                cur_a, cur_b, cur_c = a1, b1, c1

        return [cur_a, cur_b, cur_c] == target