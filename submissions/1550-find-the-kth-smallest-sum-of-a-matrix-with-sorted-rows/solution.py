class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def total(serial):
            return sum(mat[i][x] for i, x in enumerate(serial))
        start = tuple([0] * len(mat))
        h = [-total(start)]
        curr = set([start])
        visited = set()
        while curr:
            nxt = set()
            for serial in curr:
                for i in range(len(serial)):
                    if serial[i] == len(mat[0]) - 1:
                        continue
                    step = list(serial)
                    step[i] += 1
                    step = tuple(step)
                    if step in visited:
                        continue
                    visited.add(step)
                    t = -total(step)
                    if len(h) >= k:
                        if t <= h[0]:
                            continue
                        heappop(h)
                    heappush(h, t)
                    nxt.add(step)
            curr = nxt

        return -h[0]

        
