# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        node = ListNode()
        new_head = node

        while(current != None):
            total = 0
            while(current.val != 0):
                total += current.val
                current = current.next
            node.next = ListNode(total)
            node, current = node.next, current.next

        return new_head.next