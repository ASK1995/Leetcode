# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        res = []
        node_heights = defaultdict(lambda:[])
        min_col, max_col = 0, 0

        while(q):
            node, height = q.popleft()
            node_heights[height].append(node.val)
            min_col, max_col = min(min_col, height), max(max_col, height) 
            if(node.left):
                q.append((node.left, height - 1))
            if(node.right):
                q.append((node.right, height + 1))
        for values in range(min_col, max_col + 1):
            level = []
            for value in node_heights[values]:
                level.append(value)
            res.append(level)
        return res