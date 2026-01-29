class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        blacklist.sort()
        self.curr = 0
        self.n = n
        self.blacklist = []
        prev = -2
        curr = -2
        for v in blacklist:
            if v == curr + 1:
                curr += 1
            else:
                self.blacklist.append([prev, curr])
                prev = v
                curr = v
        self.blacklist.append([prev, curr])
        self.blacklist = self.blacklist[1:]
        self.idx = 0
        print(self.curr, self.n, self.blacklist)
        

    def pick(self) -> int:
        if self.blacklist:
            l, r = self.blacklist[self.idx]
            while l <= self.curr <= r:
                self.curr = (r + 1) % self.n
                self.idx = (self.idx + 1) % len(self.blacklist)
                l, r = self.blacklist[self.idx]
        ret = self.curr
        self.curr = (self.curr + 1) % self.n
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
