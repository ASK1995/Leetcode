# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        level = 0
        res = []

        while(q):
            n = len(q)
            level_nodes = []
            for i in range(n):
                node = q.popleft()
                level_nodes.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            level += 1
            if(level % 2 == 0):
                level_nodes = level_nodes[::-1]

            res.append(level_nodes)

        return res