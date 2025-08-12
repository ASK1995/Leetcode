# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaves(self, root):
        if(root == None):
            return []
        if(root.left == None and root.right == None):
            return [root.val]
        return self.leaves(root.left) + self.leaves(root.right)
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.leaves(root1)
        leaves2 = self.leaves(root2)

        return leaves1 == leaves2