class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(set)
        for e1, e2 in edges:
            g[e1].add(e2)
            g[e2].add(e1)

        curr = set([source])
        visited = set()
        while curr:
            nxt = set()
            for c in curr:
                if c == destination:
                    return True
                if c in visited:
                    continue
                visited.add(c)
                nxt.update(g[c])
            curr = nxt - visited
        
        return False
        

