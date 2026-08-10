class MyHashMap:

    def __init__(self, initial_capacity: int = 8):
        self._min_capacity = 1
        self._capacity = max(self._min_capacity, initial_capacity)
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

    def _index(self, key):
        return hash(key) % self._capacity
    
    def _resize(self, new_capacity):
        old_buckets = self._buckets

        self._capacity = new_capacity
        self._buckets = [[] for _ in range(new_capacity)]

        for bucket in old_buckets:
            for key, value in bucket:
                index = self._index(key)

                self._buckets[index].append((key, value))

    def put(self, key: int, value: int) -> None:
        index = self._index(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self._size += 1

        if self._size / self._capacity > 0.75:
            self._resize(self._capacity * 2)

    def get(self, key: int) -> int:
        index = self._index(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        
        return -1

    def remove(self, key: int) -> None:
        index = self._index(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = bucket[-1]
                bucket.pop()
                self._size -= 1
        
        if self._size / self._capacity < 0.25:
            return self._resize(self._capacity // 2)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)