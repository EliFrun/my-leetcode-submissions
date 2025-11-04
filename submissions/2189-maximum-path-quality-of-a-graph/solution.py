class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for p,c,w in edges:
            graph[p].append((c,w))
            graph[c].append((p,w))

        
        ret = 0
        def solve(n, time, s, visited):
            nonlocal ret
            if time > maxTime:
                return
            if n == 0:
                ret = max(ret, s)
            for node, weight in graph[n]:
                if n in visited:
                    solve(node, time + weight, s, visited)
                else:
                    solve(node, time + weight, s + values[n], visited | set([n]))
            return

        solve(0,0,values[0], set([0]))
        return ret
        
