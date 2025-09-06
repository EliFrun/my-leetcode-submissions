class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ret = 0
        for l, r in queries:
            counts = [0] * 16
            p1, p2 = int(log(l,4)), int(log(r, 4))

            for i in range(p1, p2 + 1):
                counts[i] = min(r, 4 ** (i + 1)) - max(l, 4 ** i)

            counts[p2] += 1

            carry = 0
            for i in range(p2, -1, -1):
                ret += counts[i] // 2
                if carry:
                    counts[i - 1] += 1
                    ret += 1
                
                counts[i - 1] += 2 * (counts[i] // 2)
                carry = counts[i] & 1
                counts[i] = 0

            ret += carry
        return ret
        
