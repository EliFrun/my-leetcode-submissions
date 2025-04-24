class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        q = []
        a = sorted(zip(capital, profits))
        i = 0
        for _ in range(k):
            while i < len(a) and a[i][0] <= w:
                heappush(q, -a[i][1])
                i += 1
            if not q:
                return w
            w += - heappop(q)

        return w
        
