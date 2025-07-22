class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for i in range(1, n):
            g[i - 1].add(i)

        def bfs():
            curr = set({0})
            visited = set()
            cnt = -1
            while curr:
                cnt += 1
                nxt = set()
                for node in curr:
                    if node == n - 1:
                        return cnt
                    if node in visited:
                        continue
                    visited.add(node)
                    nxt |= g[node]

                curr = nxt - visited
            return cnt
        
        ret = []
        for l, r in queries:
            g[l].add(r)
            ret.append(bfs())

        return ret
        
