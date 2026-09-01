# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, False)]
        heights = {}

        while stack:
            node, visited = stack.pop()
            
            if not visited:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            
            else:
                l = heights.get(node.left, 0)
                r = heights.get(node.right, 0)

                if abs(l - r) > 1:
                    return False
                
                heights[node] = max(l, r) + 1
        
        return True
