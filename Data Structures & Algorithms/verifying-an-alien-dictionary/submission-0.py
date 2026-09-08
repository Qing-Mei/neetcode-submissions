class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {letter: i for i, letter in enumerate(order)}
        
        for i in range(1, len(words)):
            prev, word = words[i - 1], words[i]

            for j in range(min(len(prev), len(word))):
                if rank[prev[j]] > rank[word[j]]:
                    return False
                if rank[prev[j]] < rank[word[j]]:
                    break
            else:
                if len(prev) > len(word):
                    return False

        return True
