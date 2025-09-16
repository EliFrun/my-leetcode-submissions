class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        @cache
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        ret = []
        for num in nums:
            while ret and gcd(num, ret[-1]) > 1:
                v = ret.pop()
                g = gcd(v, num)
                a, b = num // g, v // g
                num = g * a * b // gcd(a,b)
            ret.append(num)
        return ret
    
            
            
        
