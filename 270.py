# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        close = root.val
        min_diff = float('inf')

        while(root != None):
            diff = abs(root.val - target)
            if(diff < min_diff):
                min_diff = diff
                close = root.val
            elif(diff == min_diff and root.val != close):
                close = min(root.val, close)
            if(root.val > target):
                root = root.left
            else:
                root = root.right

        return close