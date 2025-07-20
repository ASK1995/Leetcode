# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, check):
            if root == None:
                return 0
            res = 0
            if(root.val >= check):
                res += 1
            check = max(check, root.val)
            return res + dfs(root.left, check) + dfs(root.right, check)
        return dfs(root, float('-inf'))