class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            visited.add(course)
            return True

        return all(dfs(c) for c in range(numCourses))