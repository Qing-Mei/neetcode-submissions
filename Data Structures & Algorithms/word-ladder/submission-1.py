from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)

        if endWord not in wordset:
            return 0
        
        q = deque([beginWord])
        steps = 1

        while q:
            sz = len(q)

            for _ in range(sz):
                word = q.popleft()

                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    for j in range(26):
                        new_char = chr(ord("a") + j)
                        if new_char == word[i]:
                            continue
                        new_word = word[:i] + new_char + word[i+1:]

                        if new_word in wordset:
                            q.append(new_word)
                            wordset.remove(new_word)
            
            steps += 1
        
        return 0
        