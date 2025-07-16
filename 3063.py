# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict

class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = defaultdict(lambda:0)
        while(head):
            count[head.val] += 1
            head = head.next
        res_head = ListNode()
        curr = res_head
        prev = None
        for key, value in count.items():
            curr.val = value
            curr.next = ListNode()
            prev = curr
            curr = curr.next
        curr = None
        prev.next = None
        return res_head