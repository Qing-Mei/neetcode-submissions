# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two(l1, l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            curr.next = l1 if l1 else l2
        
            return dummy.next
        
        step = 1

        while step < len(lists):
            for i in range(0, len(lists) - step, step * 2):
                lists[i] = merge_two(lists[i], lists[i + step])
                
            step *= 2
        
        return lists[0]

