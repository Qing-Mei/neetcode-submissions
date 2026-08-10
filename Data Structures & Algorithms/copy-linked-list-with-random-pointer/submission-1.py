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
            return None

        curr = head

        while curr:
            copy = Node(curr.val)

            copy.next = curr.next
            curr.next = copy

            curr = copy.next
        
        curr = head

        while curr:
            copy = curr.next

            if curr.random:
                copy.random = curr.random.next

            curr = copy.next
        
        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            nxt = copy.next

            curr.next = nxt
            copy.next = nxt.next if nxt else None

            curr = nxt
        
        return copy_head
