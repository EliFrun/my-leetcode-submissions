class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dist(dd, curr, d):
            dd[curr] = d
            for nxt in g[curr]:
                if dd[nxt] != float('inf'):
                    continue
                dist(dd, nxt, d + 1)

        

        x_dist = [float('inf')] * n
        y_dist = [float('inf')] * n
        z_dist = [float('inf')] * n

        dist(x_dist, x, 0)
        dist(y_dist, y, 0)
        dist(z_dist, z, 0)

        ret = 0
        for x,y,z in zip(x_dist,y_dist,z_dist):
            x,y,z = sorted([x,y,z])
            if x ** 2 + y ** 2 == z ** 2:
                ret += 1

        return ret
