class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        @cache
        def solve(max_string, curr_evil):
            if any([x == evil for x in curr_evil]):
                return 0
            if not max_string:
                return 1
            ret = 0
            for c in range(ord(max_string[0]) - ord('a') + 1):
                c = chr(ord('a') + c)
                nxt_max = max_string[1:] if c == max_string[0] else 'z' * (len(max_string) - 1)
                nxt_evil = []
                for evl in curr_evil:
                    s = evl + c
                    if s == evil[:len(s)]:
                        nxt_evil.append(s)
                ret += solve(nxt_max, tuple(sorted(nxt_evil + [''])))
            return ret
        
        return (solve(s2, ('',)) - solve(s1, ('',)) + (1 if evil not in s1 else 0)) % 1_000_000_007
            

        
