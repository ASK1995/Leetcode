"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        new_graph = {}
        q = deque()
        q.append(node)
        new_graph[node] = Node(node.val)

        while(q):
            node1 = q.popleft()
            for node2 in node1.neighbors:
                if node2 not in new_graph:
                    new_graph[node2] = Node(node2.val)
                    q.append(node2)
                new_graph[node1].neighbors.append(new_graph[node2])

        return new_graph[node]