class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        @cache
        def solve(x):
            if x == 0:
                return []
            ret = solve(x - 1)
            can_divide = True
            v = x
            while v > 0:
                if v % 10 == 0 or x % (v % 10) != 0:
                    can_divide = False
                    break
                v //= 10
            if can_divide:
                ret += [x]  
            return ret
        return [x for x in solve(right) if x >= left]
