class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)
        m = [set() for _ in range(n)]
        for p, c in connections:
            m[p].add(c)
            g[c].append(p)
            g[p].append(c)
        
        curr = set([0])
        visited = set()
        ret = 0
        while curr:
            nxt = set()
            for i in curr:
                if i in visited:
                    continue
                visited.add(i)
                for j in g[i]:
                    if j in visited:
                        continue
                    if j in m[i]:
                        ret += 1
                    nxt.add(j)

            curr = nxt - visited
        return ret
        
