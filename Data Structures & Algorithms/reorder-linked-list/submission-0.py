# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        x = head
        y = head.next
        u = head
        while u.next.next:
            u = u.next
        v = u.next

        u.next = None
        x.next = v
        v.next = y
        self.reorderList(y)