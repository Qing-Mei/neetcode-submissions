class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

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
        
        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(i, j, node):
            ch = board[i][j]

            if ch not in node.children:
                return
            
            node = node.children[ch]

            if node.word is not None:
                res.append(node.word)

                node.word = None

            board[i][j] = "#"

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni = i + di
                nj = j + dj

                if (0 <= ni < rows and 0 <= nj < cols and board[ni][nj] != "#"):
                    dfs(ni, nj, node)
            
            board[i][j] = ch

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        
        return res