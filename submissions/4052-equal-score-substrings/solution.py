class Solution:
    def scoreBalance(self, s: str) -> bool:
        def score(l):
            return ord(l) - ord('a') + 1

        v = sum([score(l) for l in s])
        left = 0
        if v == left:
            return True
        for c in s:
            left += score(c)
            v -= score(c)
            if v == left:
                return True

        return False
        
