# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtree_ids = {}
        next_id = 1
        target_id = None
        found = False

        def dfs(node, searching=False):
            nonlocal next_id, found

            if not node:
                return 0
            
            left_id = dfs(node.left, searching)
            right_id = dfs(node.right, searching)

            signature = (node.val, left_id, right_id)

            if signature not in subtree_ids:
                subtree_ids[signature] = next_id
                next_id += 1
            
            curr_id = subtree_ids[signature]

            if searching and curr_id == target_id:
                found = True
        
            return curr_id
        
        target_id = dfs(subRoot)

        dfs(root, searching=True)

        return found
        