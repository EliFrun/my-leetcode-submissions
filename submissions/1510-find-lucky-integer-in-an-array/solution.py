class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([c for c,v in Counter(arr).items() if c == v] + [-1])
        
