# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            res = max(res, node.val + left + right)

            return max(0, max(left, right) + node.val)
        
        dfs(root)

        return res
