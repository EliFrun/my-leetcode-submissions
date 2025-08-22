class Solution:
    def minCost(self, nodes: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for p, c, w in edges:
            g[p].append((c,w))
            g[c].append((p, 2 * w))

        cost = [float('inf')] * nodes
        curr = [(0, 0)]
        while curr:
            d, n = heappop(curr)
            if cost[n] <= d:
                continue
            cost[n] = d
            if n == nodes - 1:
                return d
            for c,w in g[n]:
                heappush(curr, (d + w, c))

        return - 1


        
