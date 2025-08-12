# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while(fast and fast.next):
            slow, fast = slow.next, fast.next.next
        prev = None
        while(slow):
            tmp = slow.next
            slow.next = prev
            prev, slow = slow, tmp
        slow = head
        res = 0
        while(prev and slow):
            res = max(res, prev.val + slow.val)
            prev, slow = prev.next, slow.next
        return res