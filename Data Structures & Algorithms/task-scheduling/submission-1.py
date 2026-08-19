from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max(count.values())
        max_count = sum(freq == max_freq for freq in count.values())

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
        