class MyHashSet:

    def __init__(self, initial_capacity: int = 8):
        self._min_capacity = max(1, initial_capacity)
        self._capacity = self._min_capacity
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

    def _index(self, key):
        return hash(key) % self._capacity
    
    def _resize(self, new_capacity: int):
        old_buckets = self._buckets

        self._capacity = new_capacity
        self._buckets = [[] for _ in range(new_capacity)]

        for bucket in old_buckets:
            for key in bucket:
                index = self._index(key)
                self._buckets[index].append(key)

    def add(self, key: int) -> None:
        index = self._index(key)
        bucket = self._buckets[index]

        if key in bucket:
            return
        
        bucket.append(key)
        self._size += 1

        if self._size / self._capacity > 0.75:
            self._resize(self._capacity * 2)

    def remove(self, key: int) -> None:
        index = self._index(key)
        bucket = self._buckets[index]

        for i, value in enumerate(bucket):
            if value == key:
                bucket[i] = bucket[-1]
                bucket.pop()
                self._size -= 1

                if self._capacity > self._min_capacity and self._size / self._capacity < 0.25:
                    self._resize(self._capacity // 2)

                return

    def contains(self, key: int) -> bool:
        index = self._index(key)
        return key in self._buckets[index]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)