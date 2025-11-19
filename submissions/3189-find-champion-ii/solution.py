class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(int)
        for p, c in edges:
            g[c] += 1

        ret = -1
        cnt = 0
        for i in range(n):
            if g[i] == 0:
                ret = i
                cnt += 1
            if cnt > 1:
                return -1
        return ret

        
