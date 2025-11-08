class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # 1 -> 0
        # 10 -> 11 -> 01 -> 00
        # 11 -> 01 -> 00
        # 100 -> 101 -> 111 -> 110 -> 010 -> 011 -> 001 -> 000

        def rebuild(s):
            if len(s) == 0:
                return 0
            if len(s) == 1:
                return 1 - int(s)
            ret = 2 ** len(s) - 1
            k = 0
            for c in s:
                if c == '1':
                    ret -= 2 ** k - 1
                k += 1
            return ret 
            
        def solve(s):
            if len(s) == 0:
                return 0
            if len(s) == 1:
                return int(s)
            if s[0] == '0':
                return solve(s[1:])
            
            return 2 ** (len(s)) - 1 - solve(s[1:])

        
        return solve(bin(n)[2:])


