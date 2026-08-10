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
            node_copy = Node(node.val)

            old_to_new[node] = node_copy

            for nei in node.neighbors:
                if nei not in old_to_new:
                    dfs(nei)
                node_copy.neighbors.append(old_to_new[nei])
            
        dfs(node)

        return old_to_new[node]
