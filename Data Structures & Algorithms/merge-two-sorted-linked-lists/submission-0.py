# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            prev = list1
            p = list1.next
            q = list2
        else:
            prev = list2
            p = list1
            q = list2.next

        dummy = prev
        while p and q:
            if p.val <= q.val:
                prev.next = p
                prev = p
                p = p.next
            else:
                prev.next = q
                prev = q
                q = q.next
        
        if p:
            prev.next = p
        if q:
            prev.next = q
        return dummy


        