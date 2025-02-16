class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]: 
        if n == 1:
            return [1]
        best = []
        def solve(lis, curr):
            nonlocal best
            if curr == 1:
                l = lis.copy()
                l[l.index(0)] = 1
                best = max(best, l)
                return l
            ret = []
            for i in range(len(lis) - curr):
                if lis[i] == 0 and lis[i + curr] == 0:
                    tmp = lis.copy()
                    tmp[i] = curr
                    tmp[i + curr] = curr
                    if best and best > [x if x > 0 else curr - 1 for x in tmp]:
                        continue
                    if s := solve(tmp, curr - 1):
                        ret = s
                        best = max(ret, best)
            return ret

        l = [0] * (2 * n - 1)
        l[0] = n
        l[n] = n
        solve(l, n - 1)
        return best

        
