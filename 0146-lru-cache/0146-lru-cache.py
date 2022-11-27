class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currSize = 0
        self.cache = {}
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def shift_to_head(self, node):
        self.delete_node(node)
        self.add_node(node)
    
    def pop_tail(self):
        node = self.tail.prev
        self.delete_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.shift_to_head(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            node = DLinkedNode()
            node.key = key
            node.value = value
            self.currSize+=1
            self.cache[key] = node
            self.add_node(node)
            if self.currSize>self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.currSize -= 1
        else:
            node.value = value
            self.shift_to_head(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)