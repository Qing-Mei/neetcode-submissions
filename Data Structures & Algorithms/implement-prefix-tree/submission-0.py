class Node:
    def __init__(self):
        self.children = [None] * 26
        self.endWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            i = ord(ch) - ord("a")
            if node.children[i] is None:
                node.children[i] = Node()
            node = node.children[i]
        
        node.endWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            i = ord(ch) - ord("a")
            if node.children[i] is None:
                return False
            node = node.children[i]
        
        return node.endWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            i = ord(ch) - ord("a")
            if node.children[i] is None:
                return False
            node = node.children[i]
        
        return True
        