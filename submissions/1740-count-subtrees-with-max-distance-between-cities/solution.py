class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        edges = [(p -1, q - 1) for p,q in edges]
        def find(g, i):
            if g[i] != i:
                parent = find(g, g[i])
                g[i] = parent
            return g[i]

        def union(g, i, j):
            u = find(g, i)
            v = find(g, j)
            if u != v:
                g[u] = v
                
        possible_graphs = set()
        for i in range(1, 2 ** (n - 1)):
            current_graph = list(range(n))
            for j, (p, q) in enumerate(edges):
                if (i >> j) & 1 == 0:
                    continue
                union(current_graph, p, q)
            
            graphs = defaultdict(set)
            for i in range(len(current_graph)):
                graphs[find(current_graph, i)].add(i)
                
            possible_graphs.update([tuple(sorted(list(v))) for v in graphs.values()])

        distances = [[0] * n for _ in range(n)]
        g = defaultdict(list)
        for p, q in edges:
            g[p].append(q)
            g[q].append(p)


        def dfs(distance, start, previous, curr):
            distances[start][curr] = distance
            for nxt in g[curr]:
                if nxt == previous:
                    continue
                dfs(distance + 1, start, curr, nxt)
        
        for i in range(n):
            dfs(0, i, -1, i)


        ret = [0] * n
        for graph in possible_graphs:
            m = 0
            for i in range(len(graph)):
                for j in range(i + 1, len(graph)):
                    m = max(m, distances[graph[i]][graph[j]])
            ret[m] += 1


        return ret[1:]

            
        
        
        
