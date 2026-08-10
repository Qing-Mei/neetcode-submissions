class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            if len(first) > len(second) and first.startswith(second):
                return ""

            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    graph[first[j]].add(second[j])
                    break

        state = {}
        order = []

        def dfs(char):
            if state.get(char, 0) == 1:
                return False

            if state.get(char, 0) == 2:
                return True

            state[char] = 1

            for nxt in graph[char]:
                if not dfs(nxt):
                    return False

            state[char] = 2
            order.append(char)
            return True

        for char in graph:
            if not dfs(char):
                return ""

        return "".join(reversed(order))
