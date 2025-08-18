# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while(q):
            q_length = len(q)
            right_element = None

            for i in range(q_length):
                element = q.popleft()
                if element:
                    q.append(element.left)
                    q.append(element.right)
                    right_element = element

            if(right_element):
                res.append(right_element.val)
        return res