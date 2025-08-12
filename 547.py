from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        res = 0

        def dfs(node):
            q = deque([node])

            while(len(q) != 0):
                node = q.pop()
                if(visited[node]):
                    continue
                visited[node] = True
                node = isConnected[node]
                for index, val in enumerate(node):
                    if val == 1:
                        q.append(index)

        for x in range(len(isConnected)):
            if(not visited[x]):
                dfs(x)
                res += 1
        return res