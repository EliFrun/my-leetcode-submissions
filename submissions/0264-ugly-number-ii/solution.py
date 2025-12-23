class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = [1]
        for i in range(n):
            v = heappop(q)
            if i == n - 1:
                return v
            while q and q[0] == v:
                heappop(q)
            heappush(q, 2 * v)
            heappush(q, 3 * v)
            heappush(q, 5 * v)

        return -1

        
