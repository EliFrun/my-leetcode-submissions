class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        str_n = str(n)

        ret = ''
        for i in range(len(str_n)):
            if i != 0 and i % 3 == 0:
                ret = '.' + ret
            ret = str_n[-i - 1] + ret

        return ret

        
