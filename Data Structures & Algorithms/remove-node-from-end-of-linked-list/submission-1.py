# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next
        pos = N - n
        if pos == 0:
            head = head.next
        else:
            prev = None
            curr = head
            while pos > 0:
                prev = curr
                curr = curr.next
                pos -= 1
            prev.next = curr.next
            curr.next = None
        return head
        