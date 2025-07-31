class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.curr = -1
        self.count = 0
        self.value = value
        

    def consec(self, num: int) -> bool:
        if num == self.curr:
            self.count += 1
        else:
            self.count = 1
            self.curr = num

        return self.curr == self.value and self.count >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
