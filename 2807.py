# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        while(b != 0):
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next
        while curr:
            gcd = self.gcd(prev.val, curr.val)
            node = ListNode(gcd)
            node.next = curr
            prev.next = node
            prev, curr = curr, curr.next
        return head