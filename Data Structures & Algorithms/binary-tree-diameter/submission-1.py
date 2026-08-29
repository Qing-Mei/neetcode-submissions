# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            res = max(l + r, res)

            return max(l, r) + 1

        dfs(root)
        return res
