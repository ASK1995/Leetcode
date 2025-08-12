# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        reset_a, reset_b = 1, 1

        while(a != None and b != None and (reset_a >= 0 or reset_b >= 0)):
            if(a == b):
                return a
            a, b = a.next, b.next
            if(a == None):
                a = headB
                reset_a -= 1

            if(b == None):
                b = headA
                reset_b -= 1

        return None