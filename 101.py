# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        while(q):
            level = []
            for i in range(len(q)):
                n = q.popleft()
                if n == None:
                    level.append('N')
                else:
                    level.append(n.val)
                if(n):
                    q.append(n.left)
                if(n):
                    q.append(n.right)
            if(level != level[::-1]):
                return False
        return True