# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  
        h = []
        heapq.heapify(h)
        for l in lists:
            while l:
                heapq.heappush(h, l.val)
                l = l.next
        
        first = ListNode(0)
        curr = first
        while h:
            curr.next = ListNode(heapq.heappop(h))
            curr = curr.next
        return first.next

        