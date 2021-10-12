class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(x)-96) for x in s)
        
        def transform(foo):
            ret = 0
            for x in foo:
                ret += int(x)
                
            return str(ret)
        
        for i in range(k):
            s = transform(s)
            
        return int(s)
        
        
