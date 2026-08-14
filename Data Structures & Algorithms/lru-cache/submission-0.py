class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val

        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()

        self.head.nxt = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev
    
    def _add_to_tail(self, node):
        tail = self.tail
        prev = tail.prev

        prev.nxt = node
        node.prev = prev

        node.nxt = tail
        tail.prev = node
    
    def _remove_head(self):
        head = self.head.nxt
        nxt = head.nxt

        self.head.nxt = nxt
        nxt.prev = self.head

        return head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
            return
        
        if len(self.cache) == self.capacity:
            removed_node = self._remove_head()
            del self.cache[removed_node.key]
        
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)
