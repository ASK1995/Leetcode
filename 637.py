# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])

        while(q):
            total = 0
            num = len(q)
            for i in range(len(q)):
                node = q.popleft()
                total += node.val
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            res.append(total/num)

        return res