"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        def dfs(node):
            if not node:
                return
            
            if node in old_to_new:
                return old_to_new[node]
            
            node_copy = Node(node.val)
            old_to_new[node] = node_copy

            node_copy.neighbors = [dfs(nei) for nei in node.neighbors]
        
            return node_copy
        
        return dfs(node)
