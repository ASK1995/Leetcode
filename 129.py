# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def total(root, val):
            if root == None:
                return 0
            val = val * 10 + root.val
            if root.left == None and root.right == None:
                return val
            return total(root.left, val) + total(root.right, val)

        return total(root, 0)