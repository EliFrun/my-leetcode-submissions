class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(set)
        for p, c in edges:
            g[c].add(p)

        @cache
        def dfs(n):
            ret = g[n]
            for x in g[n]:
                ret = ret.union(dfs(x))
            return ret

        return [sorted(list(dfs(x))) for x in range(n)]

        
