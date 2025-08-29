# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        prev, curr = None, head
        while(l1 and l2):
            total = l1.val + l2.val + carry
            carry = 0
            if(total >= 10):
                carry = 1
                total -= 10
            curr.val = total
            curr.next = ListNode()
            prev, curr, l1, l2 = curr, curr.next, l1.next, l2.next

        while(l1):
            total = l1.val + carry
            carry = 0
            if(total >= 10):
                carry = 1
                total -= 10
            curr.val = total
            curr.next = ListNode()
            prev, curr, l1 = curr, curr.next, l1.next

        while(l2):
            total = l2.val + carry
            carry = 0
            if(total >= 10):
                carry = 1
                total -= 10
            curr.val = total
            curr.next = ListNode()
            prev, curr, l2 = curr, curr.next, l2.next

        if(carry):
            curr.val = carry
            curr.next = None
        else:
            prev.next = None

        return head