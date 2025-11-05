class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for p,c in edges:
            g[p].add(c)
            g[c].add(p)

        ret = float('inf')
        visited = set()
        for i in range(1, n + 1):
            for j in g[i]:
                if j <= i:
                    continue
                for k in g[i] & g[j]:
                    if k <= j:
                        continue
                    degree = len(g[i]) + len(g[j]) + len(g[k]) - 6
                    ret = min(ret, degree)

        if ret == float('inf'):
            return -1
        return ret

