# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev, curr = node, node.next
        if(curr == None):
            prev = None
        else:
            prev.val = curr.val
            prev.next = curr.next