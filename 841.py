from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room):
            q = deque([room])

            visited = [False] * len(rooms)

            while(len(q) != 0):
                room = q.pop()
                if(visited[room]):
                    continue
                visited[room] = True
                room = rooms[room]
                for key in room:
                    q.append(key)
            return True if(all(visited[node] == True for node in range(len(rooms)))) else False

        return dfs(0)