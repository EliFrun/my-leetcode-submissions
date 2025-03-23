class Solution:
      def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[None] * n for _ in range(n)]
        for p, c, w in roads:
            adj[p][c] = w
            adj[c][p] = w

        

        distances = [10 ** 12] * n
        combos = [0] * n
        combos[0] = 1
        distances[0] = 0
        
        #bfs
        curr = [(0,0)]
        while curr:
            distance, node = heapq.heappop(curr)
            nodes = [i for i in range(n) if adj[node][i]]
            for i in nodes:
                dis = distance + adj[node][i]
                if distances[i] > dis:
                    combos[i] = combos[node]
                    distances[i] = dis
                    heapq.heappush(curr, (dis, i))
                elif distances[i] == dis:
                    combos[i] += combos[node]
        
        return combos[-1] % 1_000_000_007

        

        
