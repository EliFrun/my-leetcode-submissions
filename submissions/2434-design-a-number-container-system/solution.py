class NumberContainers:

    def __init__(self):
        self.nums = defaultdict(lambda: SortedList([]))
        self.lis = {}
        

    def change(self, index: int, number: int) -> None:
        old = self.lis.get(index, -1)
        if old != -1:
            self.nums[old].remove(index)
        self.lis[index] = number
        self.nums[number].add(index)
        

    def find(self, number: int) -> int:
        return self.nums[number][0] if self.nums[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
