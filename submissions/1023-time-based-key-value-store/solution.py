class TimeMap:

    def __init__(self):
        self.table = defaultdict(lambda: SortedList([]))
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].add((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.table[key]) == 0:
            return ''
        idx = self.table[key].bisect_left((timestamp, ''))
        idx = min(idx, len(self.table[key]) - 1)
        if self.table[key][idx][0] > timestamp:
            idx -= 1
        if idx < 0:
            return ''
        return self.table[key][idx][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
