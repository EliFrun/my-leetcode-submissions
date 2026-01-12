class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        g = defaultdict(list)
        for p, c, v in edges:
            if not online[p] or not online[c]:
                continue
            insort(g[p], (v, c))
    
        def solve(m):
            q = [(0, 0)]
            visited = set()
            while q:
                t, n = heappop(q)
                if n in visited:
                    continue
                visited.add(n)
                if n == len(online) - 1:
                    return True
                for i in range(bisect_left(g[n], (m, -1)), len(g[n])):
                    w, nn = g[n][i]
                    if w < m:
                        continue
                    if t + w > k:
                        continue
                    heappush(q, (t + w, nn))
            return False


        left, right = 0, k
        ret = -1
        while left <= right:
            middle = (left + right) // 2
            if solve(middle):
                ret = middle
                left = middle + 1
            else:
                right = middle - 1

        return ret
                
        
