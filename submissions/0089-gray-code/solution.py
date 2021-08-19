class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        
        ret = []
        foo =  self.grayCode(n - 1)
        for i in foo: 
            ret.append(i)
            
        foo.reverse()
        
        for i in foo:
            ret.append(int(2 ** (n - 1)) + i)
            
            
        return ret
            
        
