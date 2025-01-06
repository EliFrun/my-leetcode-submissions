class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0]
        while len(ret) <= n:
            ret = ret + [1 + x for x in ret]

        return ret[:n+1]
            
        
