class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = set()

        for start, end in edges:
            if start in visited:
                return start
            elif end in visited:
                return end
            visited.add(start)
            visited.add(end)

        return -1
            