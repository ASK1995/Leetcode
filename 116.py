"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return
        q = deque([root])

        while q:
            new_q = deque()
            for i in range(len(q)):
                node = q.popleft()
                if(len(q) == 0):
                    node.next = None
                else:
                    node.next = q[0]
                if(node.left):
                    new_q.append(node.left)
                if(node.right):
                    new_q.append(node.right)
            q = new_q
        return root