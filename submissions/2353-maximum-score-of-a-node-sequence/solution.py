class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for p,c in edges:
            heappush(g[p], (scores[c], c))
            if len(g[p]) > 3:
                heappop(g[p])
            heappush(g[c], (scores[p], p))
            if len(g[c]) > 3:
                heappop(g[c])

        ret = -1
        for n1, n2 in edges:
            s = scores[n1] + scores[n2]
            for score1, node1 in g[n1]:
                if node1 in (n1, n2):
                    continue
                curr = s + score1
                for score2, node2 in g[n2]:
                    if node2 in (n1, n2, node1):
                        continue
                    ret = max(ret, curr + score2)
        return ret


        
        
