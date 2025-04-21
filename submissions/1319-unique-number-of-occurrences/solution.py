class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return all(x < 2 for x in Counter(Counter(arr).values()).values())
        
        
