# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def dfs(node, high):
            nonlocal cnt

            if not node:
                return
            
            if node.val >= high:
                cnt += 1

            dfs(node.left, max(high, node.val))
            dfs(node.right, max(high, node.val))

        dfs(root, root.val)

        return cnt
