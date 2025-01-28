class Solution:
    def countDigitOne(self, n: int) -> int:
        def solve(i):
            if i <= 0:
                return 0
            if i < 10:
                return 1

            power = int(log10(i))
            left_most = i // 10 ** power
            ret = solve(i % int(10 ** power))
            ret += left_most * solve(10 ** (power) - 1)
            if left_most == 1:
                ret += i % int(10 ** power) + 1
            else:
                ret += 10 ** power

            return ret
        return solve(n)
        
        


        
