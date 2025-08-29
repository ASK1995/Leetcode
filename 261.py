class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        visited = set()
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for j in adj[node]:
                if j == prev:
                    continue
                if not dfs(j, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n