class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        curr = 0
        ret = 0
        for x,y in dimensions:
            a = x ** 2 + y ** 2
            if a > curr:
                curr = a
                ret = x * y
            elif a == curr:
                ret = max(ret, x * y)

        return ret
                
        
