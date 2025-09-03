# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, total, path):
            if(node == None):
                return
            path.append(node.val)
            if(node.left):
                dfs(node.left, total - node.val, path)
            if(node.right):
                dfs(node.right, total - node.val, path)
            if(node.left == None and node.right == None and node.val == total):
                res.append(path.copy())
            path.pop()

        dfs(root, targetSum, [])
        return res