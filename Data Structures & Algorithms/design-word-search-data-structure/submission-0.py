class Node:
    def __init__(self):
        self.children = [None] * 26
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
    
    def _dfs(self, start, root, word):
        node = root

        for i in range(start, len(word)):
            ch = word[i]
            if ch == ".":
                for child in node.children:
                    if child is not None and self._dfs(i + 1, child, word):
                            return True

                return False
            
            index = ord(ch) - ord("a")
            
            if node.children[index] is None:
                return False

            node = node.children[index]
        
        return node.endWord

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            i = ord(ch) - ord("a")
            if node.children[i] is None:
                node.children[i] = Node()
            node = node.children[i]
        
        node.endWord = True
        
    def search(self, word: str) -> bool:
        return self._dfs(0, self.root, word)

