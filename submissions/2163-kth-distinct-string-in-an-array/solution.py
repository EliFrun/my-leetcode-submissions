class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        found = 0
        for s in arr:
            if c[s] == 1:
                found += 1
            if found == k:
                return s
        
        return ""
        
