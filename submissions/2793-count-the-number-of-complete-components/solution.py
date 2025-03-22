class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graphs = []
        graph = defaultdict(set)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
            idx_n1, idx_n2 = -1, -1
            for i, g in enumerate(graphs):
                if n1 in g:
                    idx_n1 = i
                if n2 in g:
                    idx_n2 = i

            if idx_n1 == -1 and idx_n2 == -1:
                graphs.append(set([n1, n2]))
            elif idx_n1 == -1:
                graphs[idx_n2].add(n1)
            elif idx_n2 == -1:
                graphs[idx_n1].add(n2)
            else:
                if idx_n1 == idx_n2:
                    continue
                g1 = graphs.pop(max(idx_n1, idx_n2))
                g2 = graphs.pop(min(idx_n1, idx_n2))
                graphs.append(g1.union(g2))
        
        ret = 0
        for g in graphs:
            g = list(g)
            cc = True
            for i in range(len(g)):
                for j in range(i + 1, len(g)):
                    if g[i] not in graph[g[j]]:
                        cc = False
                        break
                if not cc:
                    break
            if cc:
                ret += 1

        for i in range(n):
            if len(graph[i]) == 0:
                ret += 1
        return ret



        
