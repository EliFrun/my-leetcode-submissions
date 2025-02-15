class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
            if counts[c] > 1:
                return c

        return s[-1]
        
