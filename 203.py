# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = head, head.next if head else None
        while(curr):
            if(curr.val != val):
                prev.next = curr
                prev = curr
            curr = curr.next
        if(prev):
            prev.next = curr
        if(head and head.val == val):
            return head.next
        return head