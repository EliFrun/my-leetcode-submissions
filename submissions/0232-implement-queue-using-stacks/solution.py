class MyQueue:

    def __init__(self):
        self.stk1 = []
        

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        stk2 = self.stk1[::-1]
        ret = stk2.pop()
        self.stk1 = stk2[::-1]
        return ret

    def peek(self) -> int:
        return self.stk1[0]
        

    def empty(self) -> bool:
        return len(self.stk1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
