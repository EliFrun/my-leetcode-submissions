class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dp = [0] * n
        g = defaultdict(list)
        for (p,c),pr in zip(edges, succProb):
            g[p].append((c, pr))
            g[c].append((p, pr))

        q = [(-1, start_node)]

        while q:
            prob, node = heappop(q)
            if dp[node] >= -prob:
                continue
            dp[node] = -prob
            if node == end_node:
                return -prob

            for nnode, pr in g[node]:
                heappush(q, (prob * pr, nnode))

        return dp[end_node]

        
        
