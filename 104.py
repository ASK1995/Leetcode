# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if(root == None):
                return 0
            return 1 + max(dfs(root.left), dfs(root.right))
        return dfs(root) if root else 0