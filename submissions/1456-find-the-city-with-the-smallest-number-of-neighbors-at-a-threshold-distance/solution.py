class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        m = [[-1] * n for _ in range(n)]
        for p,c,d in edges:
            m[p][c] = d
            m[c][p] = d
        
        def solve(i):
            h = [(0, i)]
            visited = set()
            while h and h[0][0] <= distanceThreshold:
                d, v = heappop(h)
                if v in visited:
                    continue
                visited.add(v)
                for i, t in enumerate(m[v]):
                    if t > 0:
                        heappush(h, (d + t, i))

            return len(visited) - 1



        return sorted(list(enumerate([solve(x) for x in range(n)])), key=lambda x: (x[1], -x[0]))[0][0]
        
