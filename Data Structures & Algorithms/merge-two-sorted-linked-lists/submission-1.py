# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def sort(list1, list2):
            if not (list1 or list2):
                return
            if list1 and not list2:
                return list1
            if list2 and not list1:
                return list2
            if list1.val >= list2.val:
                list2.next = sort(list1, list2.next)
                return list2
            if list2.val > list1.val:
                list1.next = sort(list1.next, list2)
                return list1
        return sort(list1, list2)