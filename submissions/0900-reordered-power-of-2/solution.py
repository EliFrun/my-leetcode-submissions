class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a = sorted(str(n))
        v = 1
        for _ in range(32):
            if sorted(str(v)) == a:
                return True
            v <<= 1
        return False
