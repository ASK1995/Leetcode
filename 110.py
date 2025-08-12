# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return (True, 0)
            left, left_h = dfs(node.left)
            right, right_h = dfs(node.right)
            balanced = left and right and abs(left_h - right_h) <= 1
            return (balanced, 1 + max(left_h, right_h))

        return dfs(root)[0]