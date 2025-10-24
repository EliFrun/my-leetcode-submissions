class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        l = set()
        opts = [[1], [2], [3], [1,2], [4], [1,3], [5], [1,4], [2,3], [6], [1, 2,3], [2,4], [1,5],[1,2,4]]

        for opt in opts:
            s = ''
            for v in opt:
                s += str(v) * v
            for p in permutations(s):
                l.add(int(''.join(p)))
        
        l = sorted(list(l))

        idx = bisect_right(l, n)
        return l[idx]
