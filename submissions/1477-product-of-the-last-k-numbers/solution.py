class ProductOfNumbers:

    def __init__(self):
        self.stk = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.stk = [0,1]
            return   
        self.stk.append(num * self.stk[-1])
        

    def getProduct(self, k: int) -> int:
        if len(self.stk) - 1 <= k:
            return 0 if self.stk[0] == 0 else self.stk[-1]

        return self.stk[-1] // self.stk[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
