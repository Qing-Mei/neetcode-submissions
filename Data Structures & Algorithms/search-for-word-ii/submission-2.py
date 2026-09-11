class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            
            node.word = word

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(board)
        n = len(board[0])
        res = []

        def dfs(i, j, node, visited):
            ch = board[i][j]

            if ch not in node.children:
                return False
            
            node = node.children[ch]

            if node.word:
                res.append(node.word)
                node.word = ""
                
            visited.add((i, j))

            for di, dj in dirs:
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    dfs(ni, nj, node, visited)

            visited.remove((i, j))
            
            return
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, set())
        
        return res