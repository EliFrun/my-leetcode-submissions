class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for p,c in edges:
            g[p].add(c)
            g[c].add(p)

        curr = set([1])
        visited = set()
        depth = -2
        while curr:
            depth += 1
            nxt = set()
            for node in curr:
                if node in visited:
                    continue
                visited.add(node)
                nxt |= g[node]
            curr = nxt
        
        
        return pow(2, depth - 1, 1_000_000_007)
