# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = deque()

        curr = head

        while curr is not None:
            queue.append(curr)
            curr = curr.next

        dummy = queue.popleft()
        curr = dummy

        while queue:
            curr.next = queue.pop()
            curr = curr.next

            if queue:
                curr.next = queue.popleft()
                curr = curr.next

        curr.next = None

        head = dummy