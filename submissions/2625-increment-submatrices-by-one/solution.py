class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ret = []

        queries.sort()
        for i in range(n):
            diff = [0] * (n + 1)
            for r1,c1,r2,c2 in queries:
                if r1 > i:
                    break
                if r2 < i:
                    continue
                diff[c2 + 1] -= 1
                diff[c1] += 1

            curr = 0
            l = []
            for d in diff[:-1]:
                curr += d
                l.append(curr)
            ret.append(l)
        return ret
        
