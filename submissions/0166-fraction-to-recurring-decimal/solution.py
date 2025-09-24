class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        negative = n * d < 0 and n != 0
        n, d = abs(n), abs(d)
        
        ret = str(n // d)
        n %= d
        if n == 0:
            return ('-' if negative else '') + ret

        ret += '.'
       
        i = len(ret)
        seen = {}
        while n > 0:
            if n in seen:
                ret += ')'
                ret = ret[:seen[n]] + '(' + ret[seen[n]:]
                break
            seen[n] = i
            
            if n // d == 0:
                n *= 10
            
            ret += str(n//d)
            n = n % d
            i += 1
        
        return ('-' if negative else '') + ret

        
        
