# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(root) -> int:
            nonlocal res

            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            res = max(res, root.val + l + r)

            max_path_sum = max(l, r) + root.val

            return max_path_sum if max_path_sum > 0 else 0
        
        dfs(root)

        return res
