class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.i = 0
        self.j = 0
        

    def flip(self) -> List[int]:
        ret = [self.i, self.j]
        self.i += 1
        if self.i == self.m:
            self.i = 0
            self.j += 1
            if self.j == self.n:
                self.j = 0
        return ret
        
        

    def reset(self) -> None:
        return
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
