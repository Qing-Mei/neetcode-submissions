class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.count = 1

        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
    
    def _remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        self.size -= 1
    
    def _add_to_tail(self, node):
        tail = self.tail
        prev = tail.prev

        prev.next = node
        node.prev = prev

        node.next = tail
        tail.prev = node

        self.size += 1
    
    def _remove_head(self):
        if self.size == 0:
            return None
        
        node = self.head.next
        self._remove(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.freq = {}
        self.capacity = capacity
        self.min_freq = 0
    
    def _increase_freq(self, node):
        old_freq = node.count

        self.freq[old_freq]._remove(node)

        if old_freq == self.min_freq and self.freq[old_freq].size == 0:
            self.min_freq += 1
        
        node.count += 1
        
        if node.count not in self.freq:
            self.freq[node.count] = DoublyLinkedList()
        
        self.freq[node.count]._add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._increase_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._increase_freq(node)
            return
        
        if len(self.cache) == self.capacity:
            lfu_list = self.freq[self.min_freq]
            removed_node = lfu_list._remove_head()
            del self.cache[removed_node.key]

        node = Node(key, value)
        self.cache[key] = node
        if 1 not in self.freq:
            self.freq[1] = DoublyLinkedList()
        self.freq[1]._add_to_tail(node)
        self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
