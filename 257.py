# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            print(path)
            if(node.left == None and node.right == None):
                res.append("".join(path.copy()) + str(node.val))
                return
            if(node.left):
                path.append(str(node.val) + '->')
                dfs(node.left, path)
                path.pop()
            if(node.right):
                path.append(str(node.val) + '->')
                dfs(node.right, path)
                path.pop()

        dfs(root, [])
        return res