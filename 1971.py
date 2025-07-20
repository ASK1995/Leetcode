from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False]*n

        adjacency_list = defaultdict(lambda:set())
        for start, end in edges:
            adjacency_list[start].add(end)
            adjacency_list[end].add(start)

        to_visit = [adjacency_list[source]]
        visited[source] = True
        while(to_visit):
            nodes = to_visit.pop()
            for node in nodes:
                if(not visited[node]):
                    to_visit.append(adjacency_list[node])
                    visited[node] = True
        return visited[destination]