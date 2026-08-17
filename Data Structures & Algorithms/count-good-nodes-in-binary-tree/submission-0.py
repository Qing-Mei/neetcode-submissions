# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def dfs(node, low):
            nonlocal cnt

            if not node:
                return
            
            if node.val >= low:
                cnt += 1

            dfs(node.left, max(low, node.val))
            dfs(node.right, max(low, node.val))

        dfs(root, root.val)

        return cnt
