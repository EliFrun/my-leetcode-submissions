class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for (a, b), v in zip(equations, values):
            g[a].append((b,v))
            g[b].append((a, 1/v))


        def dfs(curr, v, target, visited):
            if curr == target:
                return v
            return max([-1] + [dfs(x, v * m, target, visited.union(set([curr]))) for x, m in g[curr] if x not in visited])
            
        ret = []
        for start, end in queries:
            if start not in g or end not in g:
                ret.append(-1.0)
                continue

            ret.append(dfs(start, 1, end, set()))

        return ret

            
            
            
                

             
