# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        new_head = None
        prev = None
        current = head
        while(current):
            if(current.val not in s):
                if(new_head == None):
                    new_head = current
                    prev = current
                else:
                    prev.next = current
                    prev = current
            current = current.next
        prev.next = None
        return new_head