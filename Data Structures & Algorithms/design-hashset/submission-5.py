class MyHashSet:

    def __init__(self):
        self.capacity = 1000
        self.arr = [[] for _ in range(self.capacity)]
    
    def _index(self, key):
        return hash(key) % self.capacity

    def add(self, key: int) -> None:
        if not self.contains(key):
            i = self._index(key)

            self.arr[i].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            i = self._index(key)
            bucket = self.arr[i]

            for idx in range(len(bucket)):
                if bucket[idx] == key:
                    bucket[idx], bucket[-1] = bucket[-1], bucket[idx]
                    bucket.pop()
                    return

    def contains(self, key: int) -> bool:
        i = self._index(key)

        for num in self.arr[i]:
            if num == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)