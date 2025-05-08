class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        u = max(x, max(forbidden)) + a + b
        visited = [[False] * (u + 2) for _ in range(2)]
        curr = set([(False, 0)])
        l = 0
        while curr:
            nxt = set()
            for back, v in curr:
                if v in forbidden:
                    continue
                if v < 0:
                    continue
                if v > u:
                    continue
                if visited[back][v]:
                    continue
                if v == x:
                    return l
                visited[back][v] = True
                nxt.add((True, v + a))
                if back:
                    nxt.add((False, v - b))

            curr = nxt
            l += 1

        return -1
