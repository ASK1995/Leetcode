# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def dfs(node):
            if node == None:
                return node

            nonlocal total
            dfs(node.right)
            tmp, node.val = node.val, node.val + total
            total += tmp
            dfs(node.left)

        dfs(root)
        return root