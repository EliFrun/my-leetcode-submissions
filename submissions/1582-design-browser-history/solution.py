class BrowserHistory:

    def __init__(self, homepage: str):
        self.seq = [homepage]
        self.curr = 0
        

    def visit(self, url: str) -> None:
        self.seq = self.seq[:self.curr + 1]
        self.seq.append(url)
        self.curr = len(self.seq) - 1
        

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.seq[self.curr]
        

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.seq) - 1, self.curr + steps)
        return self.seq[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
