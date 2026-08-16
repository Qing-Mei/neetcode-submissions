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
        
        if root.val <= low or root.val >= high:
            return False
        
        return self.check(root.left, low, root.val) and self.check(root.right, root.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float("-inf"), float("inf"))
