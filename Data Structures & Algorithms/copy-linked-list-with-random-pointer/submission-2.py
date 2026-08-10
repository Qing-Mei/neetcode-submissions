"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        curr = head

        while curr:
            copy = Node(curr.val)

            copy.next = curr.random
            curr.random = copy

            curr = curr.next
        
        curr = head

        while curr:
            copy = curr.random

            copy.random = copy.next.random if copy.next else None

            curr = curr.next
        
        curr = head
        copy_head = head.random

        while curr:
            copy = curr.random

            curr.random = copy.next

            copy.next = curr.next.random if curr.next else None

            curr = curr.next
        
        return copy_head
        
