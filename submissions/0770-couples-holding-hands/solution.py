class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        @cache
        def solve(l):
            if not l:
                return 0
            
            l = list(l)
            idx_first = l.index(l[0] + 1) if l[0] % 2 == 0 else l.index(l[0] - 1)
            idx_second = l.index(l[1] + 1) if l[1] % 2 == 0 else l.index(l[1] - 1)

            if idx_first == 1:
                return solve(tuple(l[2:]))


            v = l[idx_first]
            l[idx_first] = l[1]
            l[1] = v
            ret = 1 + solve(tuple(l[2:]))
            l[1] = l[idx_first]
            l[idx_first] = v

            v = l[idx_second]
            l[idx_second] = l[0]
            l[0] = v
            ret = min(ret, 1 + solve(tuple(l[2:])))

            return ret

        return solve(tuple(row))

                
            
