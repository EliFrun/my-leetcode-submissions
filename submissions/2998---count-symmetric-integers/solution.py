class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_sym(n):
            n = str(n)
            if len(n) & 1 == 1:
                return False
            return sum([int(x) for x in n[:len(n)//2]]) == sum([int(x) for x in n[len(n)//2:]])
        
        ret = 0
        for i in range(low, high + 1): 
            ret += (1 if is_sym(i) else 0)

        return ret 
