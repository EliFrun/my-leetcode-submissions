class DeNode:
    def __init__(self, key, val, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.val = val

    def pop_self(self):
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left

    def left_nav(self):
        if not self.right:
            return str(self.val)
        return str(self.val) + '->' + self.right.left_nav()

    def right_nav(self):
        if not self.left:
            return str(self.val)
        return self.left.right_nav() + '<-' + str(self.val)
class LRUCache:

    def __init__(self, capacity: int):
        # left is most recent, right is least
        self.l = DeNode(float('-inf'), float('-inf'))
        self.r = DeNode(float('-inf'), float('-inf'))
        self.l.right = self.r
        self.r.left = self.l
        self.capacity = capacity
        self.count = 0
        self.m = {}

    def push_to_front(self, node):
        node.pop_self()
        node.right = self.l.right
        self.l.right.left = node
        node.left = self.l
        self.l.right = node
        

    def get(self, key: int) -> int:
        node = self.m.get(key, None)
        if not node:
            return -1

        self.push_to_front(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if not self.m.get(key, None):
            n = DeNode(key, value)
            self.m[key] = n
            self.push_to_front(n)
            self.count += 1
        else:
            n = self.m[key]
            n.val = value
            self.push_to_front(n)
        
        if self.count > self.capacity:
            v = self.r.left
            self.m.pop(v.key)
            self.r.left = v.left
            v.left.right = self.r
            self.count -= 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
