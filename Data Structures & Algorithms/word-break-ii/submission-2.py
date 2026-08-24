class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        
        curr.is_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)
        
        n = len(s)

        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for start in range(n):
            if not dp[start]:
                continue

            node = trie.root

            for end in range(start, n):
                ch = s[end]

                if ch not in node.children:
                    break
                
                node = node.children[ch]

                if node.is_word:
                    curr_word = s[start:end+1]

                    for prefix in dp[start]:
                        if prefix:
                            sentence = prefix + " " + curr_word
                        else:
                            sentence = curr_word
                        dp[end+1].append(sentence)
        
        return dp[n]
