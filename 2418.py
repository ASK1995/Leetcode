class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indices = [i for i in range(len(names))]
        indices.sort(key = lambda i: -1 * heights[i])
        return [names[i] for i in indices]