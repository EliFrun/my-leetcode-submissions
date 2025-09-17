class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c1, c2 = Counter(target), Counter(arr)
        
        for k in set(c1.keys()) | set(c2.keys()):
            if c1.get(k, -1) != c2.get(k, -1):
                return False
        return True
        
