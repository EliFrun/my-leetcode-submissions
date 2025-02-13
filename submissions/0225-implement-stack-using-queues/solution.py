class MyStack:

    def __init__(self):
        self.empt = []
        self.full = []
        

    def push(self, x: int) -> None:
        self.empt.append(x)
        while self.full:
            self.empt.append(self.full.pop())
        while self.empt:
            self.full.append(self.empt.pop())
        

    def pop(self) -> int:
        return self.full.pop()
        
    def top(self) -> int:
        return self.full[-1]

    def empty(self) -> bool:
        return len(self.full) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
