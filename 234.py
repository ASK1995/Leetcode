# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None
        slow = fast
        
        prev = None
        while(fast):
            temp = fast.next
            fast.next = prev
            prev, fast = fast, temp

        slow, fast = head, prev
        while(slow != None and fast != None):
            if(slow.val != fast.val):
                return False
            slow, fast = slow.next, fast.next
        return True