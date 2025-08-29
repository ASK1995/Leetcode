# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = "z"*100

        def dfs(node, path):
            nonlocal res
            if(node):
                if(node.left == None and node.right == None):
                    path.append(chr(node.val + 97))
                    res = min(res, "".join(path.copy())[::-1])
                    path.pop()
                    return
                path.append(chr(node.val + 97))
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop()

        dfs(root, [])
        return res