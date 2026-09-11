# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        sec = slow.next
        slow.next = None

        #reverse the second half
        prev = None
        curr = sec
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #prev has the head now
        #merge them alternatively
        p1,p2 = head,prev
        while p2:
            t1,t2 = p1.next,p2.next
            p1.next = p2
            p2.next = t1
            p1,p2 = t1,t2
        
        
        