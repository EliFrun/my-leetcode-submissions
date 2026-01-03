class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        M = 1_000_000_007
        curr = [1 if x == '.' else 0 for x in grid[-1]]
        nxt_p = [0] * len(grid[-1])
        left, right = 0, 0
        p = 0
        for i, c in enumerate(grid[-1]):
            if c == '#':
                continue
            while right < len(grid[-1]) and (right - i) <= d:
                p += curr[right]
                right += 1
            while (i - left) > d:
                p -= curr[left]
                left += 1
            nxt_p[i] = p - curr[i]

        curr = [x + y for x,y in zip(curr, nxt_p)]
        
        for layer in reversed(grid[:len(grid) - 1]):
            nxt = [0] * len(layer)
            left, right = 0, 0
            p = 0
            for i, c in enumerate(layer):
                while right < len(layer) and (right - i) ** 2 + 1 <= d ** 2:
                    p += curr[right]
                    right += 1
                if c == "#":
                    continue
                while (i - left) ** 2 + 1 > d ** 2:
                    p -= curr[left]
                    left += 1
                nxt[i] = p
            
            
            nxt_p = [0] * len(layer)
            left, right = 0, 0
            p = 0
            for i, c in enumerate(layer):
                while right < len(layer) and (right - i) <= d:
                    p += nxt[right]
                    right += 1
                if c == '#':
                    continue
                while (i - left) > d:
                    p -= nxt[left]
                    left += 1
                nxt_p[i] = p - nxt[i]
            curr = [x + y for x,y in zip(nxt, nxt_p)]

        return sum(curr) % M

