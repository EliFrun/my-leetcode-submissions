class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.t = 0
        self.times = {}
        self.q = []
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.times[key] = self.t
        heappush(self.q, (self.t, key))
        self.t += 1
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.c and key not in self.cache:
            while self.q[0][0] != self.times[self.q[0][1]]:
                heappop(self.q)
            t, k = heappop(self.q)
            self.cache.pop(k)
        
        self.times[key] = self.t
        heappush(self.q, (self.t, key))
        self.t += 1
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
