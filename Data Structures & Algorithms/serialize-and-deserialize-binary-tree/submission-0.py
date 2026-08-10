from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []

        q = deque([root])

        while q:
            node = q.popleft()

            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return " ".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        nodes = data.split()

        root = TreeNode(int(nodes[0]))

        q = deque([root])

        i = 1

        while q:
            curr = q.popleft()

            left_val = nodes[i]
            i += 1

            if left_val != "#":
                curr.left = TreeNode(int(left_val))
                q.append(curr.left)
            
            right_val = nodes[i]
            i += 1
            
            if right_val != "#":
                curr.right = TreeNode(int(right_val))
                q.append(curr.right)

        return root
