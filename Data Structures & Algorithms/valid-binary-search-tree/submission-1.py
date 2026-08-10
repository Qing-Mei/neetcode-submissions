# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, root, low, high):
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        if root.left:
            if root.left.val >= root.val or root.left.val <= low:
                return False
        
        if root.right:
            if root.right.val <= root.val or root.right.val >= high:
                return False

        return self.check(root.left, low, root.val) and self.check(root.right, root.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.check(root, float("-inf"), float("inf"))
