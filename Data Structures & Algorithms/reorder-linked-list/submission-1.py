# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr, prev = slow.next, None
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        p2 = prev
        curr = head

        while p2:
            p2_nxt = p2.next
            
            p2.next = curr.next
            curr.next = p2

            curr = p2.next
            p2 = p2_nxt
            