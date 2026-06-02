# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        if not head:
            return False

        slowPointer = head
        fastPointer = head.next

        if not fastPointer:
            return False

        while fastPointer != slowPointer:
            if not fastPointer or not fastPointer.next:
                return False
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        return True
