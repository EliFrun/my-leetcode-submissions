class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        def solve(i, j):
            if i == 0:
                return 'b' * j
            if j == 0:
                return 'a' * i
            if i == j:
                return 'ab' * i
            
            ret = ""
            if i > j:
                ret += 'a' * min(i, 2)
                if j > 0:
                    ret += 'b'
                return ret + solve(i - min(i, 2), j - 1)
            if j > i:
                ret += 'b' * min(j, 2)
                if i > 0:
                    ret += 'a'
                return ret + solve(i - 1, j - min(j, 2))

        return solve(a,b)
