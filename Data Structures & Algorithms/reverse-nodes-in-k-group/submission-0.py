# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            tail = curr
            n = k - 1
            while tail and n:
                tail = tail.next
                n -= 1

            if not tail:
                break
            
            for _ in range(k - 1):
                nxt = curr.next
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            
            prev = curr
            curr = curr.next
        
        return dummy.next
        