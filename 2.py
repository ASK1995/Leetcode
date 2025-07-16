# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        carry = 0
        head = ListNode()
        current = head
        prev = None

        while(head1 != None and head2 != None):
            total = head1.val + head2.val + carry
            carry = 0
            if(total >= 10):
                carry = 1
                total -= 10

            current.val = total
            current.next = ListNode()
            prev, current = current, current.next
            head1 = head1.next
            head2 = head2.next

        while(head1 != None):
            total = head1.val + carry
            carry = 0
            if(total >= 10):
                carry = 1
                total -= 10

            current.val = total
            current.next = ListNode()
            prev, current = current, current.next
            head1 = head1.next

        while(head2 != None):
            total = head2.val + carry
            carry = 0
            if(total >= 10):
                carry = 1
                total -= 10

            current.val = total
            current.next = ListNode()
            prev, current = current, current.next
            head2 = head2.next

        if(carry != 0):
            current.val = carry
            current.next = None
        else:
            prev.next = None
    
        return head