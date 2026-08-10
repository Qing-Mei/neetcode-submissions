# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        while head:
            nxt = head.next
            head.next = dummy.next
            dummy.next = head
            head = nxt

        return dummy.next
