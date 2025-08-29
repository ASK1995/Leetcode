# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0

        while(q):
            new_q = deque()
            if(level % 2 == 1):
                l, r = 0, len(q) - 1
                while(l < r):
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l, r = l + 1, r - 1

            for i in range(len(q)):
                node = q.popleft()
                if(node.left):
                    new_q.append(node.left)
                if(node.right):
                    new_q.append(node.right)
            level += 1
            q = new_q

        return root