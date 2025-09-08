class Solution:
    def minOperations(self, n: int, m: int) -> int:
        l = [True] * (2 * max(n, m))
        l[1] = False
        for i in range(2, len(l)):
            if not l[i]:
                continue
            for j in range(i + i, len(l), i):
                l[j] = False

        q = [(n, n)]
        visited = set()

        while q:
            c, h = heappop(q)
            if h in visited:
                continue
            visited.add(h)
            if h >= len(l):
                continue
            if l[h]:
                continue
            if h == m:
                return c
            s = str(h)[::-1]
            size = int(log10(h))
            for i in range(int(log10(h)) + 1):
                if s[i] != '0' or (i == size and s[i] != '1'):
                    heappush(q, (c + h - 10 ** i, h - 10 ** i))
                if s[i] != '9':
                    heappush(q, (c + h + 10 ** i, h + 10 ** i))

        return -1



