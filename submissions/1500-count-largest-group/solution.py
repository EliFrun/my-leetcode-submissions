class Solution:
    def countLargestGroup(self, n: int) -> int:
        def val(i):
            ret = 0
            div = 10 ** int(log(i))
            while i:
                ret += i // div
                i %= div
                div //= 10
            return ret

        g = defaultdict(int)
        for i in range(1, n + 1):
            g[val(i)] += 1

        return Counter(g.values())[max(g.values())]
        
