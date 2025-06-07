class Solution:
    def clearStars(self, s: str) -> str:
        i = 0
        h = []
        for i, c in enumerate(s):
            if c == '*':
                heappop(h)
            else:
                heappush(h, (c, -i))

        h.sort(key=lambda x: -x[1])

        return ''.join([x[0] for x in h])
        
