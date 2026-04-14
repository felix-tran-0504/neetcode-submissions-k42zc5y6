# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        gg = set()
        curr = head
        while curr: 
            if curr.next in gg:
                return True
            gg.add(curr.next)
            curr = curr.next
        return False