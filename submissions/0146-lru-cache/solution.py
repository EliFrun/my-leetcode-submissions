class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.usage_list = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.usage_list.remove(key)
            self.usage_list.append(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.usage_list) == self.capacity:
            if key not in self.d:
                self.d.pop(self.usage_list[0])
                self.usage_list = self.usage_list[1:]
          
        if key in self.d:
            self.usage_list.remove(key)
        
        self.d[key] = value
        self.usage_list.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
