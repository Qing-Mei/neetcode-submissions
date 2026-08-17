"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m = len(grid)
        n = len(grid[0])
        same = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] != grid[0][0]:
                    same = False
                    break
            if not same:
                break
        
        if same:
            return Node(grid[0][0], True, None, None, None, None)
        
        topleft = self.construct([grid[i][:n // 2] for i in range(m // 2)])
        topright = self.construct([grid[i][n // 2:] for i in range(m // 2)])
        bottomleft = self.construct([grid[i][:n // 2] for i in range(m // 2, m)])
        bottomright = self.construct([grid[i][n // 2:] for i in range(m // 2, m)])

        return Node(0, False, topleft, topright, bottomleft, bottomright)

