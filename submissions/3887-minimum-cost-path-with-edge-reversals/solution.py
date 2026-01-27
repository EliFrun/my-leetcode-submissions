class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for p,c,w in edges:
            g[p].append((c,w))
            g[c].append((p,2 * w))

        
        q = [(0, 0)]
        dp = [float('inf') for _ in range(n)]
        while q:
            d, node = heappop(q)
            if dp[node] <= d:
                continue

            dp[node] = d
            
            for n2, w in g[node]:
                heappush(q, (d + w, n2))
        
        return dp[-1] if dp[-1] != float('inf') else -1
