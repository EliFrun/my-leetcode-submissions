class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = []
        self.future = []
        self.curr = homepage
        

    def visit(self, url: str) -> None:
        self.hist.append(self.curr)
        self.curr = url
        self.future = []
        

    def back(self, steps: int) -> str:
        i = 0
        while self.hist and i < steps:
            self.future.append(self.curr)
            self.curr =self.hist.pop()
            i += 1
        return self.curr

        

    def forward(self, steps: int) -> str:
        i = 0
        while self.future and i < steps:
            self.hist.append(self.curr)
            self.curr = self.future.pop()
            i += 1
        return self.curr
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
