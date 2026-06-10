"""
- Use doubly linked list to keep track of LRU, with a left and right sentinal nodes to see LRU and MRU
- Use a hash map to point to the correct Node { key: node }, where Node will contain the key and value
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.next: Node | None = None
        self.previous: Node | None = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.previous = self.left

    # Insert at MRU (right)
    def insert(self, node):
        previous = self.right.previous

        previous.next = node
        self.right.previous = node

        node.next = self.right
        node.previous = previous
    
    def remove(self, node):
        next = node.next
        previous = node.previous

        previous.next = next
        next.previous = previous

        del node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # if in cache
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # LRU
            curr_node = self.left.next
            self.remove(curr_node)
            self.cache.pop(curr_node.key)

