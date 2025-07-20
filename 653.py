# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        l, r = 0, len(res) - 1
        while(l < r):
            total = res[l] + res[r]
            if(total == k):
                return True
            elif(total > k):
                 r -= 1
            else:
                l += 1
        return False