# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry:
            num1, num2 = l1.val if l1 else 0, l2.val if l2 else 0
            total = carry + num1 + num2
            carry = 0
            if(total >= 10):
                total -= 10
                carry = 1
            curr.next = ListNode(total)
            curr = curr.next
            if(l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next

        return dummy.next