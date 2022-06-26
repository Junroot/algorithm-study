class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            cur = self.cache[key]
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev = self.head
            cur.next = self.head.next
            self.head.next.prev = cur
            self.head.next = cur
            return cur.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # cur = self.head
        # while cur.next:
        #     print(cur.key, cur.value, cur.next.value)
        #     cur = cur.next
        # print("//")
        # 2. updating value
        # 3. update > recently used
        if key in self.cache:
            cur = self.cache[key]
            cur.value = value
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev = self.head
            cur.next = self.head.next
            self.head.next.prev = cur
            self.head.next = cur
            return
        if len(self.cache) >= self.capacity:
            temp = self.tail.prev.prev
            self.cache.pop(self.tail.prev.key)
            self.tail.prev = temp
            temp.next = self.tail
        cur = Node(key, value, self.head, self.head.next)
        self.cache[key] = cur
        # 1. confused two lines
        self.head.next.prev = cur
        self.head.next = cur

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)