class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        @functools.cache
        def solve(leading_zero, i):
            if i == len(num) - 1:
                return [num[i]]
            ret = (
                [num[i] + '+' + x for x in solve(True, i+1)] +
                [num[i] + '-' + x for x in solve(True, i+1)] +
                [num[i] + '*' + x for x in solve(True, i+1)]
            )
            if num[i] != '0':
                ret += [num[i] + x for x in solve(False, i + 1)]
            elif leading_zero == False:
                ret += [num[i] + x for x in solve(False, i + 1)]
            return ret
        
        return [x for x in solve(True, 0) if eval(x) == target]
        
        
