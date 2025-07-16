class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current, max_alt = 0, 0

        for alt in gain:
            current += alt
            max_alt = max(max_alt, current)
        
        return max_alt