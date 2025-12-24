class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        g = defaultdict(list)
        for p,c in edges:
            g[c].append(p)

        for k,v in g.items():
            if len(v) > 1:
                visited = set()
                p = v[0]
                while p:
                    if p in visited:
                        return [v[0], k]
                    visited.add(p)
                    p = g[p][0] if g[p] else None
                return [v[1], k]


        # find cycle
        visited = set()
        curr = 1
        while curr not in visited:
            visited.add(curr)
            curr = g[curr][0]

        main_cycle = set()
        visited = set()
        while curr not in visited:
            visited.add(curr)
            curr = g[curr][0]

        for p,c in reversed(edges):
            if p in visited and c in visited:
                return [p, c]
        return [-1, -1]
                
                

            
        
