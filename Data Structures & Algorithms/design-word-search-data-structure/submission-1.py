from collections import deque

class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        
        curr.is_word = True

    def search(self, word: str) -> bool:
        q = deque([self.root])

        curr = self.root

        for ch in word:
            next_q = deque()

            while q:
                node = q.popleft()

                if ch == ".":
                    for child in node.children.values():
                        next_q.append(child)
                else:
                    if ch in node.children:
                        next_q.append(node.children[ch])
            
            if not next_q:
                return False
        
            q = next_q
        
        return any(node.is_word for node in q)
