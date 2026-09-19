from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word} # V + E
        indegree = {char: 0 for char in graph}
        # n length of words
        # time
        # n * min(len(word)) + V + E
        # space v + e
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]

            if len(first) > len(second) and first.startswith(second):
                return ""
            
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    if second[j] not in graph[first[j]]:
                        graph[first[j]].add(second[j])
                        indegree[second[j]] += 1
                    break
        
        q = deque()
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)
        
        order = []

        while q:
            char = q.popleft()
            order.append(char)

            for nxt in graph[char]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        if len(order) != len(indegree):
            return ""
        
        return "".join(order)

