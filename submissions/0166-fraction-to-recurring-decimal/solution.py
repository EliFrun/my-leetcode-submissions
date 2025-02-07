class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        neg = False
        if n < 0:
            neg = not neg
            n *= -1
        if d < 0:
            neg = not neg
            d *= -1
       
        whole = n // d
        rem = (n % d) * 10
        ret = ('-' if neg else '') + str(whole)
        if rem == 0:
            if whole == 0:
                return '0'
            return ret
        ret += '.'
        i = len(ret)
        seen = {}
        while rem > 0:
            if rem in seen:
                return ret[:seen[rem]] + '(' + ret[seen[rem]:] + ')'
            seen[rem] = i
            ret += str(rem // d)
            rem = (rem % d) * 10
            i += 1

        return ret

        
        
