class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.m1 = SortedList()
        self.m2 = defaultdict(SortedList)
        self.m3 = {}
        for s,m,p in entries:
            self.m2[m].add((p,s))
            self.m3[(s,m)] = p
        

    def search(self, movie: int) -> List[int]:
        return [s for p, s in self.m2[movie][:5]]
        

    def rent(self, shop: int, movie: int) -> None:
        p = self.m3[(shop, movie)]
        self.m1.add([p, shop, movie])
        self.m2[movie].remove((p, shop))
        

    def drop(self, shop: int, movie: int) -> None:
        p = self.m3[(shop, movie)]
        self.m2[movie].add((p, shop))
        self.m1.remove([p, shop, movie])
        

    def report(self) -> List[List[int]]:
        return [[s, m] for p,s,m in self.m1[:5]]
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
