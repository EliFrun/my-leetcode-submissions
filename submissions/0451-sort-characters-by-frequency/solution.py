class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(lambda: 0)
        
        for i in s:
            d[i] += 1
            
            
        foo = list(d.items())
        foo.sort(key=lambda x: x[1], reverse=True)
        
        ret = ""
        for key, value in foo:
            ret += key * value
            
        return ret
