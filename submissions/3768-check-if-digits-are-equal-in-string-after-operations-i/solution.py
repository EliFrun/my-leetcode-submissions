class Solution:
    def hasSameDigits(self, s: str) -> bool:
        curr = [int(x) for x in s]
        while len(curr) > 2:
            nxt = []
            for i in range(len(curr) - 1):
                nxt.append((curr[i] + curr[i + 1]) % 10)
            curr = nxt
        return curr[0] == curr[1]
        
