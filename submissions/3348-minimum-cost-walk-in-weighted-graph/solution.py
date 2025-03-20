class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graphs = []
        for l, r, w in edges:
            left_idx, right_idx = -1, -1
            for i, (g, s) in enumerate(graphs):
                if l in g:
                    left_idx = i
                if r in g:
                    right_idx = i
            if left_idx == -1 and right_idx == -1:
                graphs.append([set([l, r]), w])
            elif left_idx == -1:
                graphs[right_idx][0].add(l)
                graphs[right_idx][1] &= w
            elif right_idx == -1:
                graphs[left_idx][0].add(r)
                graphs[left_idx][1] &= w
            else:
                if left_idx == right_idx:
                    graphs[left_idx][1] &= w
                else:
                    g1, s1 = graphs.pop(max(left_idx, right_idx))
                    g2, s2 = graphs.pop(min(left_idx, right_idx))
                    graphs.append([g1.union(g2), s1 & s2 & w])
        
        n_map = defaultdict(lambda: -1)

        for i, (g, s) in enumerate(graphs):
            for node in g:
                n_map[node] = i

        ret = []
        for n1, n2 in query:
            if n_map[n1] == -1 or n_map[n2] == -1:
               ret.append(-1)
            elif n_map[n1] != n_map[n2]:
                ret.append(-1)
            else:
                ret.append(graphs[n_map[n1]][1])

        return ret 

            
        
