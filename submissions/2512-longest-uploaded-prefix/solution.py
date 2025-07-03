class LUPrefix:

    def __init__(self, n: int):
        self.curr = 0
        self.lis = [False] * n
        

    def upload(self, video: int) -> None:
        self.lis[video - 1] = True
        while self.curr < len(self.lis) and self.lis[self.curr]:
            self.curr += 1
        

    def longest(self) -> int:
        return self.curr
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
