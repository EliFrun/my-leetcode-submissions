class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(ss):
            return ss == ss[::-1]

        @functools.cache
        def solve(ss):
            if len(ss) == 1:
                return [[ss]]
            if ss == '':
                return [[]]
            ret = []
            for i in range(1, len(ss) + 1):
                if is_pal(ss[:i]):
                    ret.extend([[ss[:i]] + x for x in solve(ss[i:])])

            return ret

        return solve(s)

            
