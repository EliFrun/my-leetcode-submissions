class Solution:

    def __init__(self, w: List[int]):
        self.l = SortedList()
        curr = 0
        for i, num in enumerate(w):
            curr += num
            self.l.add((curr, i))
        

    def pickIndex(self) -> int:
        r = random.random() * self.l[-1][0]
        idx = self.l.bisect_left((r, -1))
        return self.l[idx][1]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
