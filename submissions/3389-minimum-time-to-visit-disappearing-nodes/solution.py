class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = defaultdict(list)
        for p,c,d in edges:
            g[p].append((c, d))
            g[c].append((p, d))
        h = [(0, 0)]
        answers = [float('inf')] * n
        while h:
            d, idx = heappop(h)
            if answers[idx] <= d:
                continue
            if d >= disappear[idx]:
                answers[idx] = -1
                continue
            answers[idx] = d
            for node, time in g[idx]:
                heappush(h, (d + time, node))
            
        return [x if x != float('inf') else -1 for x in answers]

        
