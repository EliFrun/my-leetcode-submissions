class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for b, w in edges:
            g[w].add(b)
        
        count = 0
        best = -1
        for i in range(n):
            if len(g[i]) == 0:
                best = i
                count += 1
            if count > 1:
                return -1

        return best
