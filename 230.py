# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = [root]

        while(l):
            while(root):
                l.append(root)
                root = root.left
            root = l.pop()
            k -= 1
            if 0 == k:
                return root.val
            root = root.right