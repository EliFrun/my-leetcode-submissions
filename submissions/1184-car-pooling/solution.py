class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))
        h = []
        curr = 0
        for n, f, e in trips:
            while h and h[0][0] <= f:
                _, c = heappop(h)
                curr -= c
            if curr + n <= capacity:
                curr += n
                heappush(h, (e, n))
            else:
                return False

        return True
        
