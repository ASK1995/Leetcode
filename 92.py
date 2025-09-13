# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        index = 1

        while(index != left):
            prev, curr = curr, curr.next
            index += 1

        h1, h2  = None, curr
        while(index != right + 1):
            tmp = h2.next
            h2.next = h1
            h1, h2 = h2, tmp
            index += 1
        prev.next = h1
        curr.next = h2

        return dummy.next