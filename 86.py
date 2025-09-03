# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(0), ListNode(0)
        h1, h2 = dummy1, dummy2
        curr = head

        while(curr):
            if(curr.val < x):
                h1.next = curr
                h1 = h1.next
            else:
                h2.next = curr
                h2 = h2.next
            curr = curr.next
        h1.next = dummy2.next
        h2.next = None
        head = dummy1.next
        return head