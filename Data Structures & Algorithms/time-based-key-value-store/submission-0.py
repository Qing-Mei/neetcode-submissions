from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        lst = self.store[key]

        l, r = 0, len(lst)

        while l < r:
            m = (l + r) // 2

            if lst[m][0] > timestamp:
                r = m
            else:
                l = m + 1
        
        return lst[l - 1][1] if l else ""
