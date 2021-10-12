class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def count(a):
            d = defaultdict(int)
            for i in a:
                d[i] += 1
                
            return d
        
        def sub(a, b):
            for k, v in b.items():
                a[k] -= v
                
            return a
            
            
        return all(x >= 0 for x in sub(count(magazine), count(ransomNote)).values())
