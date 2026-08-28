# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        last_visited = None
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack[-1]

            if node.right and node.right is not last_visited:
                curr = node.right
            else:
                stack.pop()
                res.append(node.val)
                last_visited = node
            
        return res
